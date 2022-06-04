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

## Using this Cookbook

If you're new to `Polars` we reccommend reading through this Cookbook in its entirity to properly familiarize yourself with the `DataFrame` library.

| Step | Content     | Description |
| ---- | ----------- | ----------- |
| 1 | Walk-through   | A 5 minute walkthrough of basic `Polars` usage introducing you to the Eager API. |
| 2 | Fundamentals   | More information on concepts to solidify your understanding of the library and important design decisions `Polars` makes. |
| 3 | Guides         | Additional documentation and recipes with details guiding users through various use cases for `Polars`. |
| 4 | References     | More material to refer to while learning and using `Polars`. |

## Walk-through

The following walk-through leverages the `Polars` Eager API to process data using common `DataFrame` library user behavior.

### 1. Create a `DataFrame`

In `Polars` a `DataFrame` is a collection of columns (more specifically `Series`) containing data. See more about the columnar memory format [here](https://arrow.apache.org/docs/format/Columnar.html), as it's a fundamental topic for `Polars` users.

To keep things simple, we've already created a list of `datetime`s for our `DataFrame` called `my_datetime_list`.

```python
{{#include ../examples/dataframe/dataset.py:2:13}}
df.sample()
```

```text
{{#include ../outputs/dataframe/df.txt}}
```

### 2. Add data to your `DataFrame`

Add a column to the `DataFrame`'s collection. Using [`pl.lit()`](POLARS_PY_REF_GUIDE/api/polars.lit.html?#polars.lit) we can add a new column populated with a `Literal`.

```python
{{#include ../examples/dataframe/add_col.py:4:}}
df.sample(3)
```

```text
{{#include ../outputs/dataframe/df_column_added.txt}}
```

### 3. Modify your `DataFrame`

Replace data using conditional expressions and chaining methods.

```python
{{#include ../examples/dataframe/replace.py:4:}}
df.tail()
```

```text
{{#include ../outputs/dataframe/df_replaced.txt}}
```

### 4. Update data types

**Use the [`Categorical`](POLARS_PY_REF_GUIDE/api/polars.datatypes.Categorical.html?#polars.datatypes.Categorical) type and do some string ops**. With the `Categorical` data type we want to plan ahead here. If we want to perform common ops like `join`s on our cats, we'll need to create this data within the [`StringCache`](POLARS_PY_REF_GUIDE/api/polars.StringCache.html#polars.StringCache) context manager.

```python
with pl.StringCache():
    # create your pl.Categorical here 👋
    # ...
```

For the purposes of this walk-through we'll just use [`toggle_string_cache`](POLARS_PY_REF_GUIDE/api/polars.toggle_string_cache.html#polars.toggle_string_cache).

```python
# collect strings in same cache for Categorical comparisons
pl.toggle_string_cache(True)

{{#include ../examples/dataframe/datatypes.py:4:}}
df.tail()
```

```text
{{#include ../outputs/dataframe/df_new_datatypes.txt}}
```

As a `Polars` user, it's up to you how you formulate your workflow. `StringCache` context managers provide a clean approach to overhead management if you need it.

👇 To **estimate** your `DataFrame`'s size [in bytes](POLARS_PY_REF_GUIDE/api/polars.DataFrame.estimated_size.html?#polars.DataFrame.estimated_size) and access its types.

```python
df.estimated_size(), df.dtypes
```

```text
{{#include ../outputs/dataframe/df_info.txt}}
```

### Use a `join`

Becuase we're using `toggle_string_cache` to create our `Categorical` data for each `DataFrame`, we can perform a `join` to bring in the IDs for each `color`.

```python
{{#include ../examples/dataframe/cat_join.py:5:}}
color_ids
```

```text
{{#include ../outputs/dataframe/color_ids.txt}}
```

### Use a `groupby`

We have `datetime`s in this `DataFrame`. Perform `groupby` operations on your `DataFrame` at **embarrassingly parallel** speeds, another fundemantal topic for a new `Polars` user.

```python
{{#include ../examples/dataframe/date_groupby.py:5:}}
res.head()
```

```text
{{#include ../outputs/dataframe/dates_groupby_res.txt}}
```

> This User Guide is under construction.
>
> Coming: IO behaviors and gut check.
