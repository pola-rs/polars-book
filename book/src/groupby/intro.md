# GroupBy

One of the most important operations in a DataFrame library is of course grouping data, also called "split-apply-combine".
Polars has excellent performance in this operation. This is due to:

* Efficient implementations in Rust
* The "split" and the "apply" phase are executed multi-threaded. 

The "apply" phase is embarrassingly parallel,
and as long you don't use python functions that block the GIL your code will run in parallel. The image below shows the
different phases.

![](https://raw.githubusercontent.com/ritchie46/img/master/polars/split-apply-combine-par.svg)

For the hashing operations done in the "split" phase, Polars uses a multi-threaded lock free approach that can be visualized
by the schema drawn below.

![](https://raw.githubusercontent.com/ritchie46/img/master/polars/lock-free-hash.svg)

These two parallel phases, make that the GROUPBY and the JOIN operation in Polars are blazingly fast! If you want to read
more about this [read my blog post on the subject](https://www.ritchievink.com/blog/2021/02/28/i-wrote-one-of-the-fastest-dataframe-libraries/)

## Don't kill the parallelization
We've all heard that Python is slow. In a GROUPBY in Polars this is especially true. Besides the overhead of running "slow"
Python bytecode, Python has a `Mutex`, called the **GIL (Global Interpreter Lock)**. This means that if you use a `lambda` or custom
Python function in the **embarrasingly parallel apply phase**, you don't only run Python code, 
but you are also preventing other threads from executing that function.

This all feels really limiting, because we often need those `lambda`'s in a GROUPBY, right? Don't worry, you can still 
use them, but just know that you are paying for the **bytecode** AND the **GIL**.

## Lazy API DSL
To mitigate this, Polars has a powerful DSL that can be used in the lazy API, but **also in an the eager GROUPBY API**.
Read more about this in the next paragraph.
