# Expression contexts

You cannot use an expression anywhere. An expression needs a context, the available contexts are:

- selection: `df.select([..])`
- groupy aggregation: `df.groupby(..).agg([..])`
- hstack/ add columns: `df.with_columns([..])`

## Syntactic sugar

The reason for such a context, is that you actually are using the Polars lazy API, even if you use it in eager.
For instance this snippet:

```python
df.groupby("foo").agg([pl.col("bar").sum()])
```

actually desugars to:

```python
(df.lazy().groupby("foo").agg([pl.col("bar").sum()])).collect()
```

This allows Polars to push the expression into the query engine, do optimizations, and cache intermediate results.

## Select context

In the `select` context the selection applies expressions over columns. The expressions in this context must produce `Series` that are all
the same length or have a length of `1`.

A `Series` of a length of `1` will be broadcasted to match the height of the `DataFrame`.
Note that a `select` may produce new columns that are aggregations, combinations of expressions, or literals.

#### Selection context

```python
{{#include ../examples/expressions/select_context_2.py:4:}}
print(out)
```

```text
{{#include ../outputs/expressions/select_context_2.txt}}
```

**Add columns**

Adding columns to a `DataFrame` using `with_columns` is also the `selection` context.

```python
{{#include ../examples/expressions/with_column_context_1.py:4:}}
print(out)
```

```text
{{#include ../outputs/expressions/wc_context_1.txt}}
```

## Groupby context

In the `groupby` context expressions work on groups and thus may yield results of any length (a group may have many members).

```python
{{#include ../examples/expressions/agg_context_1.py:4:}}
print(out)
```

```text
{{#include ../outputs/expressions/agg_context_1.txt}}
```

Besides the standard `groupby`, `groupby_dynamic`, and `groupby_rolling` are also entrances to the `groupby context`.
