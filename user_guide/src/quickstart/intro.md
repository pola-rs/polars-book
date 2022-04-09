# Getting started

## Installation

Installing `Polars` is just a simple `pip install` away.

```shell
$ pip install polars
```

All binaries are pre-built for `Python` v3.6+.

## Quick start

Below we show a simple snippet that parses a CSV file, filters it, and finishes with a
groupby operation.

```python
import polars as pl

df = pl.read_csv("https://j.mp/iriscsv")
print(df.filter(pl.col("sepal_length") > 5)
      .groupby("species")
      .agg(pl.all().sum())
)
```

The snippet above will output:

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

As we can see, `Polars` pretty-prints the output object, including the column name and
datatype as headers.

## Lazy quick start

If we want to run this query in `lazy Polars` we'd write:

```python
import polars as pl

print(
    pl.read_csv("https://j.mp/iriscsv")
    .lazy()
    .filter(pl.col("sepal_length") > 5)
    .groupby("species")
    .agg(pl.all().sum())
    .collect()
)
```

When the data is stored locally, we can also use `scan_csv` to run the query in lazy polars.

## References

If you want to dive right into the `Python` API docs, check the [the reference docs](POLARS_PY_REF_GUIDE).

### Lazy API

The lazy API builds a query plan. Nothing is executed until you explicitly ask `Polars`
to execute the query (via `LazyFrame.collect()`, or `LazyFrame.fetch()`). This provides
`Polars` with the entire context of the query, allowing optimizations and choosing the
fastest algorithm given that context.

Going from eager to lazy is often as simple as starting your query with `.lazy()` and ending with `.collect()`.

So the eager snippet above would become:

```python
(
    df.lazy()
    .filter(pl.col("sepal_length") > 5)
    .groupby("species")
    .agg(pl.all().sum())
    .collect()
)
```
