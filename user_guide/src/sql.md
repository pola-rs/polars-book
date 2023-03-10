# Polars SQL

## Starting the SQL Context

You can query a `Polars` `LazyFrame` with SQL.
The first step is to initialize a SQL context, and register a `LazyFrame` with it.

Let's load some data and initialize the SQL context:

```python
{{#include examples/sql/sql_1.py}}
```

Polars supports a single SQL context per thread, and the registered dataframe should be a `LazyFrame`.
You can call the register function multiple time for each of your LazyFrame.

## Running your SQL queries 🚀🚀

You run your SQL queries with `SQLContext.query`.

```python
{{#include examples/sql/sql_2.py:6:}}
```

```text
{{#include outputs/sql/sql_2.txt}}
```
