# Getting started

## Installation

Installing `Polars` is just a simple `pip install` away.

```shell
$ pip install polars
```

All binaries are pre-built for `Python` v3.6+.

## Quick start

Below we show a simple snippet that parses a CSV file, filters it, and finishes with a groupby operation.
As mentioned before the eager API must feel very similar to users familiar to `Pandas`.
The lazy API is more declarative, and describes *what one wants* instead of *how one wants it*. 

```python
import polars as pl
```

### Eager quickstart

```python
dataset = pl.read_csv("https://j.mp/iriscsv")
df = dataset[dataset["sepal_length"] > 5].groupby("species").sum()
```

### Lazy quickstart

```python
q = (
    pl.scan_csv("iris.csv")
    .filter(pl.col("sepal_length") > 5)
    .groupby("species")
    .agg(pl.col("*").sum())
)
df = q.collect()
```

In both cases, the snippet will output:

```text
shape: (3, 5)
╭──────────────┬──────────────────┬─────────────────┬──────────────────┬─────────────────╮
│ species      ┆ sepal_length_sum ┆ sepal_width_sum ┆ petal_length_sum ┆ petal_width_sum │
│ ---          ┆ ---              ┆ ---             ┆ ---              ┆ ---             │
│ str          ┆ f64              ┆ f64             ┆ f64              ┆ f64             │
╞══════════════╪══════════════════╪═════════════════╪══════════════════╪═════════════════╡
│ "virginica"  ┆ 324.5            ┆ 146.2           ┆ 273.1            ┆ 99.6            │
├╌╌╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┤
│ "versicolor" ┆ 281.9            ┆ 131.8           ┆ 202.9            ┆ 63.3            │
├╌╌╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┤
│ "setosa"     ┆ 116.9            ┆ 81.7            ┆ 33.2             ┆ 6.1             │
╰──────────────┴──────────────────┴─────────────────┴──────────────────┴─────────────────╯
```

As we can see, `Polars` pretty-prints the output object, including the column name and datatype as headers.

## References

If you want to dive right into the `Python` API docs, refer to [the index](POLARS_PY_REF_GUIDE) or follow one of the following direct links:

### Eager API

The eager API is very similar to [`Pandas`](https://pandas.pydata.org/).
Operations are executed directly in an imperative manner.
The important data structures are the [`DataFrame`](POLARS_PY_REF_GUIDE/frame.html#polars.frame.DataFrame) and the [`Series`](POLARS_PY_REF_GUIDE/series.html#polars.series.Series)

### Lazy API

The lazy API builds a query plan.
Nothing is executed until you explicitly ask `Polars` to execute the query (via `LazyFrame.collect()`, or `LazyFrame.fetch()`).
This provides `Polars` with the entire context of the query, allowing optimizations and choosing the fastest algorithm given that context.

The important data structure is here the [`LazyFrame`](POLARS_PY_REF_GUIDE/lazy/index.html#polars.lazy.LazyFrame), a `DataFrame` abstraction lazily keeping track of the query plan.

Arguments given to a `LazyFrame` can be constructed by building simple to complex queries following the [`Expr` API](POLARS_PY_REF_GUIDE/lazy/index.html#polars.lazy.Expr).
See the examples in the [How can I?](/howcani/intro.html) section of the guide.
