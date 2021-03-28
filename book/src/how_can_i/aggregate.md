# How can I aggregate?

Aggregations can be done in a `.select` or a `.with_column`/`with_columns` method.

If you want to do a specific aggregation on all columns you can use the wildcard expression: `.select(col("*").sum())`

The aggregation functions available are (may be outdated):
* [count](POLARS_API_LINK/lazy/index.html#polars.lazy.Expr.count)
* [first](POLARS_API_LINK/lazy/index.html#polars.lazy.Expr.first)
* [last](POLARS_API_LINK/lazy/index.html#polars.lazy.Expr.last)
* [list](POLARS_API_LINK/lazy/index.html#polars.lazy.Expr.list)
* [mean](POLARS_API_LINK/lazy/index.html#polars.lazy.Expr.mean)
* [median](POLARS_API_LINK/lazy/index.html#polars.lazy.Expr.median)
* [n_unique](POLARS_API_LINK/lazy/index.html#polars.lazy.Expr.n_unique)
* [min](POLARS_API_LINK/lazy/index.html#polars.lazy.Expr.min)
* [max](POLARS_API_LINK/lazy/index.html#polars.lazy.Expr.max)
* [sum](POLARS_API_LINK/lazy/index.html#polars.lazy.Expr.sum)
* [var](POLARS_API_LINK/lazy/index.html#polars.lazy.Expr.var)
* [std](POLARS_API_LINK/lazy/lazy/index.html#polars.lazy.Expr.std)
* [quantile](POLARS_API_LINK/lazy/index.html#polars.lazy.LazyFrame.quantile)


## Examples
```python
{{#include ../examples/how_can_i/aggregate.py:1:7}}

reddit.fetch()
```

```text
{{#include ../outputs/how_can_i_aggregate.txt}}
```
