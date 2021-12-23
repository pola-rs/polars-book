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

You cannot use an expression everywhere. An expression needs a context from which it can
select the column `"foo"` to start with.

#### Selection context

```python
{{#include ../examples/expressions/select_context_2.py:4:}}
```

## Groupby context

You can use expression during `groupby` aggregations:

```python
{{#include ../examples/expressions/agg_context_1.py:4:}}
print(df)
```

```text
{{#include ../outputs/expressions/agg_context_1.txt}}
```

## Add columns context

And finally you can use expressions to add one or multiple columns to an existing `DataFrame`

```python
{{#include ../examples/expressions/with_column_context_1.py:4:}}
print(df)
```

```text
{{#include ../outputs/expressions/wc_context_1.txt}}
```
