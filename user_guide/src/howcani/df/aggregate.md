# Aggregate

Column aggregations can done be within a `.select()` context. You can also use `.with_column()` and `.with_columns()`
contexts.

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

See more in the [API docs of Expr](POLARS_PY_REF_GUIDE/expression.html#aggregation).
