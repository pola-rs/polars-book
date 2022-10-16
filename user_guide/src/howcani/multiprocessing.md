# Combining Polars with Python's multiprocessing

TLDR: if you find that using Python's built-in `multiprocessing` module together with Polars results in your program hanging, you should make sure you are using `spawn`, not `fork`, as the starting method:

```python
with get_context("spawn").Pool() as pool:
   pool.map(my_fun, ["input1", "input2", ...])
```


## When not to use multiprocessing
Before we dive into the details, it is important to emphasize that Polars has been build from the start to lever all your CPU cores. 
It does this by executing computations which can be done in parallel in separate threads.
For example, requesting two expressions in a `select` statement can be done in parallel, with the results only being combined at the end.
Another example is aggregating a value within groups using `groupby().agg(<expr>)`, each group can be evaluated separately.
It is very unlikely that the `multiprocessing` module can improve your code performance in these cases.

See optimizations/lazy/intro.html for more optimizations.

## When to use multiprocessing
Although Polars is multithreaded, other libraries may be single-threaded.
When the other library is the bottleneck, and the problem at hand is parallelizable, it makes sense to use multiprocessing to speed up.

## The problem with the default multiprocessing config
### Summary
The [Python multiprocessing documentation](https://docs.python.org/3/library/multiprocessing.html) lists the three methods a process pool can be created:
1. spawn
2. fork
3. forkserver

The description of fork reads (as of 2022-10-15):
> The parent process uses os.fork() to fork the Python interpreter. The child process, when it begins, is effectively identical to the parent process. All resources of the  parent are inherited by the child process. Note that safely forking a multithreaded process is problematic.

> Available on Unix only. The default on Unix.

The short summary is: Polars is multithreaded as to provide strong performance out-of-the-box.
Thus, it cannot be combined with `fork`.
If you are on Unix (Linux, BSD, etc), you are using `fork`, unless you explicitly override it.

The reason you may not have encountered this before is that pure Python code, and most Python libraries, are (mostly) single threaded.
Alternatively, you are on Windows or MacOS, on which `fork` is not even available as a method (for MacOS it was up to Python 3.7).


### Example

The problem with `fork` is in the copying of the parent's process.
Consider the example below, which is a slightly modified example posted on the [Polars issue tracker](https://github.com/pola-rs/polars/issues/3144):

```python
import multiprocessing
import polars as pl


def test_sub_process(df: pl.DataFrame, job_id):
    df_filtered = df.filter(pl.col('a') > 0)
    print(f"Filtered (job_id: {job_id})", df_filtered, sep="\n")


def create_dataset():
    return pl.DataFrame(
        {
            "a": [0, 2, 3, 4, 5],
            "b": [0, 4, 5, 56, 4]
        }
    )


def setup():
   # some setup work
   df = create_dataset()
   df.write_parquet("/tmp/test.parquet")


def main():
    test_df = pl.read_parquet("/tmp/test.parquet")

    for i in range(0, 5):
        proc = multiprocessing.get_context('spawn').Process(
            target=test_sub_process,
            args=(test_df, i)
        )
        proc.start()
        proc.join()

        print(f"Executed sub process {i}")


if __name__ == '__main__':
    setup()
    main()
```

Using `fork` as the method,  instead of `spawn` will cause a dead lock.

The fork method is equivalent to calling `os.fork()`, which is a system call as defined in [the POSIX standard](https://pubs.opengroup.org/onlinepubs/9699919799/functions/fork.html):

> A process shall be created with a single thread. If a multi-threaded process calls fork(), the new process shall contain a replica of the calling thread and its entire address space, possibly including the states of mutexes and other resources. Consequently, to avoid errors, the child process may only execute async-signal-safe operations until such time as one of the exec functions is called.

So what happens in the code example? 
For reading the file, `pl.read_parquet` is used, which involves locking the file to be able to read it.
Then `os.fork()` is called, copying the state of the parent process, including mutexes.
Thus all child processes will copy the file lock in an acquired state, leaving them hanging indefinetely waiting for the lock to be released, which never happens.

What makes debugging these issues tricky is that `fork` can work.
Change the example to not having the call to `pl.read_parquet`:

```python
... 

def main():
    test_df = create_dataset()

    for i in range(0, 5):
        proc = multiprocessing.get_context('fork').Process(
            target=test_sub_process,
            args=(test_df, i)
        )
        proc.start()
        proc.join()

        print(f"Executed sub process {i}")


if __name__ == '__main__':
    main()
```

This works fine. 
Therefore debugging these issues in larger code bases, i.e. not the small toy examples here, can be a real pain, as a seemingly unrelated change can break your multiprocessing code.
In general, one should never use the `fork` start method with multithreaded libraries.

So why is `fork` even available in Python to start with?
Probably because of historical reasons: `spawn` was added to Python in version 3.4.
And because it is faster than `spawn`: `spawn` is effectively `fork` + creating a brand new Python process without the locks using [https://pubs.opengroup.org/onlinepubs/9699919799/functions/exec.html](execve). 
Hence the warning in the Python docs that it is slower: there is more overhead to `spawn`.
However, in almost all cases, one would like to use multiple processes to speed up computations that take multiple minutes or even hours, meaning the overhead is negligible in the grand scheme of things. 
And more importantly, it actually works in combination with multithreaded libraries.


## References
[1] https://docs.python.org/3/library/multiprocessing.html

[2] https://pythonspeed.com/articles/python-multiprocessing/

[3] https://pubs.opengroup.org/onlinepubs/9699919799/functions/fork.html

[4] https://bnikolic.co.uk/blog/python/parallelism/2019/11/13/python-forkserver-preload.html
