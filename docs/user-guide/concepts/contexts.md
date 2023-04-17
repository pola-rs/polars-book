# Contexts

Polars has developed its own Domain Specific Language (DSL) for transforming data. The language is very easy to use and allows for complex queries that remain human readable. The two core components of the language are Contexts and Expressions, the latter we will cover in the next section. 

A context, as implied by the name, refers to the context in which an expression needs to be evaluated. There are three main contexts [^1]: 

1. Selection: `df.select([..])`, `df.with_columns([..])`
1. Filtering: `df.filter()`
1. Groupy / Aggregation: `df.groupby(..).agg([..])`

The examples below are performed on the following `DataFrame`:

=== ":fontawesome-brands-python: Python"
    ``` python
    --8<-- "user-guide/python/concepts/contexts.py:dataframe"
    ```


```
shape: (5, 4)
┌──────┬───────┬──────────┬────────┐
│ nrs  ┆ names ┆ random   ┆ groups │
│ ---  ┆ ---   ┆ ---      ┆ ---    │
│ i64  ┆ str   ┆ f64      ┆ str    │
╞══════╪═══════╪══════════╪════════╡
│ 1    ┆ foo   ┆ 0.154163 ┆ A      │
│ 2    ┆ ham   ┆ 0.74005  ┆ A      │
│ 3    ┆ spam  ┆ 0.263315 ┆ B      │
│ null ┆ egg   ┆ 0.533739 ┆ C      │
│ 5    ┆ null  ┆ 0.014575 ┆ B      │
└──────┴───────┴──────────┴────────┘
```

## Select 

In the `select` context the selection applies expressions over columns. The expressions in this context must produce `Series` that are all the same length or have a length of 1.

A `Series` of a length of 1 will be broadcasted to match the height of the `DataFrame`. Note that a select may produce new columns that are aggregations, combinations of expressions, or literals.

=== ":fontawesome-brands-python: Python"
    ``` python
    --8<-- "user-guide/python/concepts/contexts.py:select"
    ```

```
shape: (5, 4)
┌─────┬───────┬────────────┬────────┐
│ nrs ┆ names ┆ first name ┆ 10xnrs │
│ --- ┆ ---   ┆ ---        ┆ ---    │
│ i64 ┆ str   ┆ str        ┆ f64    │
╞═════╪═══════╪════════════╪════════╡
│ 11  ┆ null  ┆ foo        ┆ 27.5   │
│ 11  ┆ egg   ┆ foo        ┆ 27.5   │
│ 11  ┆ foo   ┆ foo        ┆ 27.5   │
│ 11  ┆ ham   ┆ foo        ┆ 27.5   │
│ 11  ┆ spam  ┆ foo        ┆ 27.5   │
└─────┴───────┴────────────┴────────┘
```

As you can see from the query the `select` context is very powerfull and allows you to perform arbitrary expressions independent (and in parallel) of each other. 

Similarly to the `select` statement there is the `with_columns` statement which also is an entrance to the selection context. The main difference is that `with_columns` retains the original columns and adds new ones while `select` drops the original columns.

=== ":fontawesome-brands-python: Python"
    ``` python
    --8<-- "user-guide/python/concepts/contexts.py:with_columns"
    ```

```
shape: (5, 6)
┌──────┬───────┬──────────┬────────┬─────────┬───────┐
│ nrs  ┆ names ┆ random   ┆ groups ┆ nrs_sum ┆ count │
│ ---  ┆ ---   ┆ ---      ┆ ---    ┆ ---     ┆ ---   │
│ i64  ┆ str   ┆ f64      ┆ str    ┆ i64     ┆ u32   │
╞══════╪═══════╪══════════╪════════╪═════════╪═══════╡
│ 1    ┆ foo   ┆ 0.154163 ┆ A      ┆ 11      ┆ 5     │
│ 2    ┆ ham   ┆ 0.74005  ┆ A      ┆ 11      ┆ 5     │
│ 3    ┆ spam  ┆ 0.263315 ┆ B      ┆ 11      ┆ 5     │
│ null ┆ egg   ┆ 0.533739 ┆ C      ┆ 11      ┆ 5     │
│ 5    ┆ null  ┆ 0.014575 ┆ B      ┆ 11      ┆ 5     │
└──────┴───────┴──────────┴────────┴─────────┴───────┘
```

## Filter 

In the `filter` context you filter the existing dataframe based on arbritary expression which evaluates to the `Boolean` data type. 

=== ":fontawesome-brands-python: Python"
    ``` python
    --8<-- "user-guide/python/concepts/contexts.py:filter"
    ```

```
shape: (2, 4)
┌──────┬───────┬──────────┬────────┐
│ nrs  ┆ names ┆ random   ┆ groups │
│ ---  ┆ ---   ┆ ---      ┆ ---    │
│ i64  ┆ str   ┆ f64      ┆ str    │
╞══════╪═══════╪══════════╪════════╡
│ 3    ┆ spam  ┆ 0.263315 ┆ B      │
│ 5    ┆ null  ┆ 0.014575 ┆ B      │
└──────┴───────┴──────────┴────────┘
```

## Groupby / Aggregation 

In the `groupby` context expressions work on groups and thus may yield results of any length (a group may have many members).

=== ":fontawesome-brands-python: Python"
    ``` python
    --8<-- "user-guide/python/concepts/contexts.py:groupby"
    ```

```
shape: (3, 5)
┌────────┬──────┬───────┬────────────┬────────────────┐
│ groups ┆ nrs  ┆ count ┆ random_sum ┆ reversed names │
│ ---    ┆ ---  ┆ ---   ┆ ---        ┆ ---            │
│ str    ┆ i64  ┆ u32   ┆ f64        ┆ list[str]      │
╞════════╪══════╪═══════╪════════════╪════════════════╡
│ B      ┆ 8    ┆ 2     ┆ 0.263315   ┆ [null, "spam"] │
│ C      ┆ null ┆ 1     ┆ 0.533739   ┆ ["egg"]        │
│ A      ┆ 3    ┆ 2     ┆ 0.894213   ┆ ["ham", "foo"] │
└────────┴──────┴───────┴────────────┴────────────────┘
```

As you can see from the result all expressions are applied to the group defined by the `groupby` context. Besides the standard `groupby`, `groupby_dynamic`, and `groupby_rolling` are also entrances to the groupby context.

[^1]: There is an additional List context which is covered later in this guide. But for simplicity, we leave this out of scope for now. 