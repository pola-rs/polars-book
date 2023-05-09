# Introduction

While Polars does support writing queries in SQL, it's recommended that users familiarize themselves with the [expression syntax](../concepts/expressions.md) for more readable and expressive code. As a primarily DataFrame library, new features will typically be added to the expression API first. However, if you already have an existing SQL codebase or prefer to use SQL, Polars also offers support for SQL queries.


!!! note Execution
    In Polars, there is no separate SQL engine because Polars translates SQL queries into [expressions](../concepts/expressions.md), which are then executed using its built-in execution engine. This approach ensures that Polars maintains its performance and scalability advantages as a native DataFrame library while still providing users with the ability to work with SQL queries.

## Context

Polars uses the `SQLContext` to manage SQL queries . The context contains a dictionary mapping table names to their corresponding datasets[^1]. The example below starts a `SQLContext`:

{{code_block('user-guide/sql/intro','context',['SQLContext'])}}

```python exec="on" session="user-guide/sql"
--8<-- "python/user-guide/sql/intro.py:setup"
--8<-- "python/user-guide/sql/intro.py:context"
```

Using the `register` function, we can register DataFrames in the `SQLContext` by name. This allows us to access the DataFrame data using the corresponding table name in SQL queries.

{{code_block('user-guide/sql/intro','register',['SQLregister','SQLquery'])}}

```python exec="on" result="text" session="user-guide/sql"
--8<-- "python/user-guide/sql/intro.py:register"
```

[^1]: Additionally it also tracks the [common table expressions](./cte.md) as well. 

## Compatibility  

Polars does not support the full SQL language, in Polars you are allowed to:

- Write a `CREATE` statements `CREATE TABLE xxx AS ...`
- Write a `SELECT` statements with all generic elements (`GROUP BY`, `WHERE`,`ORDER`,`LIMIT`,`JOIN`, ...)
- Write Common Table Expressions (CTE's) (`WITH tablename AS`)
- Show an overview of all tables `SHOW TABLES`

The following is not yet supported:

- `INSERT`, `UPDATE` or `DELETE` statements
- `HAVING` clauses in aggregate queries
- Table aliasing (e.g. `SELECT p.Name from pokemon AS p`)
- Meta queries such as `ANALYZE`, `EXPLAIN`

In the upcoming sections we will cover each of the statements in more details.