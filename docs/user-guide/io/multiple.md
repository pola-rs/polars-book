## Dealing with multiple files.

`Polars` can deal with multiple files differently depending on your needs and memory strain.

Let's create some files to give use some context:

=== ":fontawesome-brands-python: Python"
    ``` python
    --8<-- "user-guide/python/io/multiple.py:create"
    ```

## Reading into a single `DataFrame`

To read multiple files into a single `DataFrame`, we can use globbing patterns:

=== ":fontawesome-brands-python: Python"
    ``` python
    --8<-- "user-guide/python/io/multiple.py:read"
    ```

```python exec="on" result="text" session="user-guide/io/multiple"
--8<-- "user-guide/python/io/multiple.py:create"
--8<-- "user-guide/python/io/multiple.py:read"
--8<-- "user-guide/python/io/multiple.py:creategraph"
```

To see how this works we can take a look at the query plan. Below we see that all files are read separately and
concatenated into a single `DataFrame`. `Polars` will try to parallelize the reading.

=== ":fontawesome-brands-python: Python"
    ``` python
    --8<-- "user-guide/python/io/multiple.py:graph"
    ```

![multiple](../../src/images/multiple.png)

## Reading and processing in parallel

If your files don't have to be in a single table you can also build a query plan for each file and execute them in parallel
on the `Polars` thread pool.

All query plan execution is embarrassingly parallel and doesn't require any communication.

=== ":fontawesome-brands-python: Python"
    ``` python
    --8<-- "user-guide/python/io/multiple.py:glob"
    ```

```python exec="on" result="text" session="user-guide/io/multiple"
--8<-- "user-guide/python/io/multiple.py:glob"
```