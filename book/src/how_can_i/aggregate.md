# How can I aggregate?

Aggregations can be done in a `.select` or a `.with_column`/`with_columns` method.

If you want to do a specific aggregation on all columns you can use the wildcard expression: `.select(col("*").sum())`

The aggregation functions available are (may be outdated):
* [avg](https://ritchie46.github.io/polars/pypolars/lazy/index.html#pypolars.lazy.avg)
* [count](https://ritchie46.github.io/polars/pypolars/lazy/index.html#pypolars.lazy.avg)
* [first](https://ritchie46.github.io/polars/pypolars/lazy/index.html#pypolars.lazy.avg)
* [last](https://ritchie46.github.io/polars/pypolars/lazy/index.html#pypolars.lazy.avg)
* [list](https://ritchie46.github.io/polars/pypolars/lazy/index.html#pypolars.lazy.avg)
* [mean](https://ritchie46.github.io/polars/pypolars/lazy/index.html#pypolars.lazy.avg)
* [median](https://ritchie46.github.io/polars/pypolars/lazy/index.html#pypolars.lazy.avg)
* [n_unique](https://ritchie46.github.io/polars/pypolars/lazy/index.html#pypolars.lazy.avg)
* [min](https://ritchie46.github.io/polars/pypolars/lazy/index.html#pypolars.lazy.avg)
* [max](https://ritchie46.github.io/polars/pypolars/lazy/index.html#pypolars.lazy.avg)
* [sum](https://ritchie46.github.io/polars/pypolars/lazy/index.html#pypolars.lazy.avg)
* [var](https://ritchie46.github.io/polars/pypolars/lazy/index.html#pypolars.lazy.avg)
* [std](https://ritchie46.github.io/polars/pypolars/lazy/index.html#pypolars.lazy.avg)
* [quantile](https://ritchie46.github.io/polars/pypolars/lazy/index.html#pypolars.lazy.LazyFrame.quantile)


## Examples
```python
{{#include ../examples/how_can_i/aggregate.py:1:7}}

reddit.fetch()
```

```text
{{#include ../outputs/how_can_i_aggregate.txt}}
```
