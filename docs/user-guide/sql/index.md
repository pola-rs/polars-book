# Polars SQL

## Starting the SQL Context

You can query a `Polars` `LazyFrame` with SQL.
The first step is to initialize a SQL context, and register a `LazyFrame` with it.

Let's load some data and initialize the SQL context:

=== ":fontawesome-brands-python: Python"
    ``` python
    --8<-- "user-guide/python/sql/index.py:df"
    ```

```python exec="on" result="text" session="user-guide/sql/index"
--8<-- "user-guide/python/sql/index.py:df"
```


Polars supports a single SQL context per thread, and the registered dataframe should be a `LazyFrame`.
You can call the register function multiple time for each of your LazyFrame.

## Running your SQL queries 🚀🚀

You run your SQL queries with `SQLContext.query`.

=== ":fontawesome-brands-python: Python"
    ``` python
    --8<-- "user-guide/python/sql/index.py:query"
    ```

```python exec="on" result="text" session="user-guide/sql/index"
--8<-- "user-guide/python/sql/index.py:query"
```
