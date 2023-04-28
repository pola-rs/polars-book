# SQL

## Starting the SQL Context

You can query a `Polars` `LazyFrame` with SQL.
The first step is to initialize a SQL context, and register a `LazyFrame` with it.

Let's load some data and initialize the SQL context:


{{code_block('user-guide/sql/index','df',['SQLContext'])}}

```python exec="on" result="text" session="user-guide/sql/index"
--8<-- "python/user-guide/sql/index.py:df"
```


Polars supports a single SQL context per thread, and the registered dataframe should be a `LazyFrame`.
You can call the register function multiple time for each of your LazyFrame.

## Running your SQL queries 🚀🚀

You run your SQL queries with `SQLContext.query`.

{{code_block('user-guide/sql/index','query',['SQLquery'])}}

```python exec="on" result="text" session="user-guide/sql/index"
--8<-- "python/user-guide/sql/index.py:query"
```
