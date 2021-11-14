# Aggregate

Column Aggregations can be within via a `.select()` or the `.with_column()`/`.with_columns()`
context.

Aggregation on all columns can be performed using the wildcard expression:
`.select(pl.col("*").sum())`.

For instance:

```python
{{#include ../../examples/aggregate/snippet.py}}
```

yielding:

```text
{{#include ../../outputs/aggregate/output.txt}}
```

See more in the [API docs of Expr](POLARS_PY_REF_GUIDE/expression.html#aggregation)
