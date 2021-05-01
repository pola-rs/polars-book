# Aggregate

Aggregations can be done via a `.select()` or the `.with_column()`/`.with_columns()`
methods.

Aggregation on all columns can be performed using the wildcard expression:
`.select(col("*").sum())`.

The available aggregation functions:

- [`.count()`](POLARS_PY_REF_GUIDE/lazy/index.html#polars.lazy.Expr.count)
- [`.first()`](POLARS_PY_REF_GUIDE/lazy/index.html#polars.lazy.Expr.first)
- [`.last()`](POLARS_PY_REF_GUIDE/lazy/index.html#polars.lazy.Expr.last)
- [`.list()`](POLARS_PY_REF_GUIDE/lazy/index.html#polars.lazy.Expr.list)
- [`.mean()`](POLARS_PY_REF_GUIDE/lazy/index.html#polars.lazy.Expr.mean)
- [`.median()`](POLARS_PY_REF_GUIDE/lazy/index.html#polars.lazy.Expr.median)
- [`.n_unique()`](POLARS_PY_REF_GUIDE/lazy/index.html#polars.lazy.Expr.n_unique)
- [`.min()`](POLARS_PY_REF_GUIDE/lazy/index.html#polars.lazy.Expr.min)
- [`.max()`](POLARS_PY_REF_GUIDE/lazy/index.html#polars.lazy.Expr.max)
- [`.sum()`](POLARS_PY_REF_GUIDE/lazy/index.html#polars.lazy.Expr.sum)
- [`.var()`](POLARS_PY_REF_GUIDE/lazy/index.html#polars.lazy.Expr.var)
- [`.std()`](POLARS_PY_REF_GUIDE/lazy/lazy/index.html#polars.lazy.Expr.std)
- [`.quantile()`](POLARS_PY_REF_GUIDE/lazy/index.html#polars.lazy.LazyFrame.quantile)

For instance:

```python
{{#include ../../examples/aggregate/snippet.py}}
```

yielding:

```text
{{#include ../../outputs/aggregate/output.txt}}
```
