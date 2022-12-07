# Polars quick exploration

This quick exploration guide is written for new users of Polars. The goal is to provide an overview of the most common functions and capabilities of the package. In this guide we will provide several examples. At the end of every part there is a link to relevant parts of the Polars Book with more information and the API reference guide.

In this exploration guide we will go through the follow topics:

- [Installation and Import](#installation-and-import)
- [Object creation](#object-creation)
  - [From scratch](#from-scratch)
  - [From files](#from-files)
- [Viewing data](#viewing-data)
- [Expressions](#expressions)
  - [Select](#select-statement)
  - [Filter](#filter)
  - [With_columns](#with_columns)
  - [Groupby](#groupby)
  - [Combining operations](#combining-operations)
- [Combining dataframes](#combining-dataframes)  
  - [Join](#join)
  - [Concat](#concat)
- [Remaining topics](#remaining-topics)

## Installation and Import

Install `Polars` in your (virtual) environment with the following command:

```shell
pip install -U polars
```

Import `Polars` as follows:

```python
import polars as pl

# to enrich the examples in this quickstart with dates
from datetime import datetime, timedelta 
# to generate data for the examples
import numpy as np 
```

## Object creation

### From scratch

Creating a simple `Series` or `Dataframe` is easy and very familiar to other packages.

You can create a `Series` in Polars by providing a `list` or a `tuple`.

```python
# with a tuple
series = pl.Series("a", [1, 2, 3, 4, 5])

print(series)
```

    shape: (5,)
    Series: 'a' [i64]
    [
        1
        2
        3
        4
        5
    ]

```python
# with a list
series = pl.Series([1, 2, 3, 4, 5])

print(series)
```

    shape: (5,)
    Series: '' [i64]
    [
        1
        2
        3
        4
        5
    ]

A `DataFrame` is created from a `dict` or a collection of `dicts`.

```python
dataframe = pl.DataFrame({"integer": [1, 2, 3], 
                          "date": [
                              (datetime(2022, 1, 1)), 
                              (datetime(2022, 1, 2)), 
                              (datetime(2022, 1, 3))
                          ], 
                          "float":[4.0, 5.0, 6.0]})

print(dataframe)
```

    shape: (3, 3)
    ┌─────────┬─────────────────────┬───────┐
    │ integer ┆ date                ┆ float │
    │ ---     ┆ ---                 ┆ ---   │
    │ i64     ┆ datetime[μs]        ┆ f64   │
    ╞═════════╪═════════════════════╪═══════╡
    │ 1       ┆ 2022-01-01 00:00:00 ┆ 4.0   │
    ├╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌┤
    │ 2       ┆ 2022-01-02 00:00:00 ┆ 5.0   │
    ├╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌┤
    │ 3       ┆ 2022-01-03 00:00:00 ┆ 6.0   │
    └─────────┴─────────────────────┴───────┘

Additional information

- Link to `Series` in the Reference guide: [link](https://pola-rs.github.io/polars/py-polars/html/reference/series/index.html)
- Link to `DataFrames` in the Reference guide: [link](https://pola-rs.github.io/polars/py-polars/html/reference/dataframe/index.html)

### From files

In Polars we can also read files and create a `DataFrame`. In the following examples we write the output of the `DataFrame` from the previous part to a specific file type (`csv`, `json` and `parquet`). After that we will read it and print the output for inspection.

#### csv

```python
dataframe.write_csv('output.csv')
```

```python
df_csv = pl.read_csv('output.csv')

print(df_csv)
```

    shape: (3, 3)
    ┌─────────┬────────────────────────────┬───────┐
    │ integer ┆ date                       ┆ float │
    │ ---     ┆ ---                        ┆ ---   │
    │ i64     ┆ str                        ┆ f64   │
    ╞═════════╪════════════════════════════╪═══════╡
    │ 1       ┆ 2022-01-01T00:00:00.000000 ┆ 4.0   │
    ├╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌┤
    │ 2       ┆ 2022-01-02T00:00:00.000000 ┆ 5.0   │
    ├╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌┤
    │ 3       ┆ 2022-01-03T00:00:00.000000 ┆ 6.0   │
    └─────────┴────────────────────────────┴───────┘

As we can see above, Polars made the datetimes a `string`. We can tell Polars to parse dates, when reading the csv, to ensure the date becomes a datetime. The example can be found below:

```python
df_csv_with_dates = pl.read_csv('output.csv', parse_dates=True)

print(df_csv_with_dates)
```

    shape: (3, 3)
    ┌─────────┬─────────────────────┬───────┐
    │ integer ┆ date                ┆ float │
    │ ---     ┆ ---                 ┆ ---   │
    │ i64     ┆ datetime[μs]        ┆ f64   │
    ╞═════════╪═════════════════════╪═══════╡
    │ 1       ┆ 2022-01-01 00:00:00 ┆ 4.0   │
    ├╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌┤
    │ 2       ┆ 2022-01-02 00:00:00 ┆ 5.0   │
    ├╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌┤
    │ 3       ┆ 2022-01-03 00:00:00 ┆ 6.0   │
    └─────────┴─────────────────────┴───────┘

#### json

```python
dataframe.write_json('output.json')
```

```python
df_json = pl.read_json('output.json')

print(df_json)
```

    shape: (3, 3)
    ┌─────────┬─────────────────────┬───────┐
    │ integer ┆ date                ┆ float │
    │ ---     ┆ ---                 ┆ ---   │
    │ i64     ┆ datetime[μs]        ┆ f64   │
    ╞═════════╪═════════════════════╪═══════╡
    │ 1       ┆ 2022-01-01 00:00:00 ┆ 4.0   │
    ├╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌┤
    │ 2       ┆ 2022-01-02 00:00:00 ┆ 5.0   │
    ├╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌┤
    │ 3       ┆ 2022-01-03 00:00:00 ┆ 6.0   │
    └─────────┴─────────────────────┴───────┘

#### parquet

```python
dataframe.write_parquet('output.parquet')
```

```python
df_parquet = pl.read_parquet('output.parquet')

print(df_parquet)
```

    shape: (3, 3)
    ┌─────────┬─────────────────────┬───────┐
    │ integer ┆ date                ┆ float │
    │ ---     ┆ ---                 ┆ ---   │
    │ i64     ┆ datetime[μs]        ┆ f64   │
    ╞═════════╪═════════════════════╪═══════╡
    │ 1       ┆ 2022-01-01 00:00:00 ┆ 4.0   │
    ├╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌┤
    │ 2       ┆ 2022-01-02 00:00:00 ┆ 5.0   │
    ├╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌┤
    │ 3       ┆ 2022-01-03 00:00:00 ┆ 6.0   │
    └─────────┴─────────────────────┴───────┘

Additional information

- Read more about `IO` in the Polars Book: [link](../howcani/io/intro.html)
- Link to `IO` in the Reference guide: [link](https://pola-rs.github.io/polars/py-polars/html/reference/io.html)

## Viewing data

This part focuses on viewing data in a `DataFrame`. We first create a `DataFrame` to work with.

```python
df = pl.DataFrame({"a": np.arange(0, 8), 
                   "b": np.random.rand(8), 
                   "c": [datetime(2022, 12, 1) + timedelta(days=idx) for idx in range(8)],
                   "d": [1, 2.0, np.NaN, np.NaN, 0, -5, -42, None]
                  })

print(df)
```

    shape: (8, 4)
    ┌─────┬──────────┬─────────────────────┬───────┐
    │ a   ┆ b        ┆ c                   ┆ d     │
    │ --- ┆ ---      ┆ ---                 ┆ ---   │
    │ i64 ┆ f64      ┆ datetime[μs]        ┆ f64   │
    ╞═════╪══════════╪═════════════════════╪═══════╡
    │ 0   ┆ 0.220182 ┆ 2022-12-01 00:00:00 ┆ 1.0   │
    ├╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌┤
    │ 1   ┆ 0.750839 ┆ 2022-12-02 00:00:00 ┆ 2.0   │
    ├╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌┤
    │ 2   ┆ 0.634639 ┆ 2022-12-03 00:00:00 ┆ NaN   │
    ├╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌┤
    │ 3   ┆ 0.67404  ┆ 2022-12-04 00:00:00 ┆ NaN   │
    ├╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌┤
    │ 4   ┆ 0.102818 ┆ 2022-12-05 00:00:00 ┆ 0.0   │
    ├╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌┤
    │ 5   ┆ 0.896408 ┆ 2022-12-06 00:00:00 ┆ -5.0  │
    ├╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌┤
    │ 6   ┆ 0.062943 ┆ 2022-12-07 00:00:00 ┆ -42.0 │
    ├╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌┤
    │ 7   ┆ 0.108093 ┆ 2022-12-08 00:00:00 ┆ null  │
    └─────┴──────────┴─────────────────────┴───────┘

The `head` function shows by default the first 5 rows of a `DataFrame`. You can specify the number of rows you want to see (e.g. `df.head(10)`).

```python
df.head(5)
```

    shape: (5, 4)
    ┌─────┬──────────┬─────────────────────┬─────┐
    │ a   ┆ b        ┆ c                   ┆ d   │
    │ --- ┆ ---      ┆ ---                 ┆ --- │
    │ i64 ┆ f64      ┆ datetime[μs]        ┆ f64 │
    ╞═════╪══════════╪═════════════════════╪═════╡
    │ 0   ┆ 0.220182 ┆ 2022-12-01 00:00:00 ┆ 1.0 │
    ├╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌┤
    │ 1   ┆ 0.750839 ┆ 2022-12-02 00:00:00 ┆ 2.0 │
    ├╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌┤
    │ 2   ┆ 0.634639 ┆ 2022-12-03 00:00:00 ┆ NaN │
    ├╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌┤
    │ 3   ┆ 0.67404  ┆ 2022-12-04 00:00:00 ┆ NaN │
    ├╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌┤
    │ 4   ┆ 0.102818 ┆ 2022-12-05 00:00:00 ┆ 0.0 │
    └─────┴──────────┴─────────────────────┴─────┘

The `tail` function shows the last 5 rows of a `DataFrame`. You can also specificy the number of rows you want to see, similar to `head`.

```python
df.tail(5)
```

    shape: (5, 4)
    ┌─────┬──────────┬─────────────────────┬───────┐
    │ a   ┆ b        ┆ c                   ┆ d     │
    │ --- ┆ ---      ┆ ---                 ┆ ---   │
    │ i64 ┆ f64      ┆ datetime[μs]        ┆ f64   │
    ╞═════╪══════════╪═════════════════════╪═══════╡
    │ 3   ┆ 0.67404  ┆ 2022-12-04 00:00:00 ┆ NaN   │
    ├╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌┤
    │ 4   ┆ 0.102818 ┆ 2022-12-05 00:00:00 ┆ 0.0   │
    ├╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌┤
    │ 5   ┆ 0.896408 ┆ 2022-12-06 00:00:00 ┆ -5.0  │
    ├╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌┤
    │ 6   ┆ 0.062943 ┆ 2022-12-07 00:00:00 ┆ -42.0 │
    ├╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌┤
    │ 7   ┆ 0.108093 ┆ 2022-12-08 00:00:00 ┆ null  │
    └─────┴──────────┴─────────────────────┴───────┘

If you want to get an impression of the data of your `DataFrame`, you can also use `sample`. With `sample` you get an *n* number of random rows from the `DataFrame`.

```python
df.sample(n=3)
```

    shape: (3, 4)
    ┌─────┬──────────┬─────────────────────┬──────┐
    │ a   ┆ b        ┆ c                   ┆ d    │
    │ --- ┆ ---      ┆ ---                 ┆ ---  │
    │ i64 ┆ f64      ┆ datetime[μs]        ┆ f64  │
    ╞═════╪══════════╪═════════════════════╪══════╡
    │ 0   ┆ 0.220182 ┆ 2022-12-01 00:00:00 ┆ 1.0  │
    ├╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌┤
    │ 1   ┆ 0.750839 ┆ 2022-12-02 00:00:00 ┆ 2.0  │
    ├╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌┤
    │ 7   ┆ 0.108093 ┆ 2022-12-08 00:00:00 ┆ null │
    └─────┴──────────┴─────────────────────┴──────┘

`Describe` returns summary statistics of your `DataFrame`. It will provide several quick statistics if possible.

```python
df.describe()
```

    shape: (7, 5)
    ┌────────────┬─────────┬──────────┬────────────────────────────┬───────┐
    │ describe   ┆ a       ┆ b        ┆ c                          ┆ d     │
    │ ---        ┆ ---     ┆ ---      ┆ ---                        ┆ ---   │
    │ str        ┆ f64     ┆ f64      ┆ str                        ┆ f64   │
    ╞════════════╪═════════╪══════════╪════════════════════════════╪═══════╡
    │ count      ┆ 8.0     ┆ 8.0      ┆ 8                          ┆ 8.0   │
    ├╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌┤
    │ null_count ┆ 0.0     ┆ 0.0      ┆ 0                          ┆ 1.0   │
    ├╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌┤
    │ mean       ┆ 3.5     ┆ 0.431245 ┆ null                       ┆ NaN   │
    ├╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌┤
    │ std        ┆ 2.44949 ┆ 0.340445 ┆ null                       ┆ NaN   │
    ├╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌┤
    │ min        ┆ 0.0     ┆ 0.062943 ┆ 2022-12-01 00:00:00.000000 ┆ -42.0 │
    ├╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌┤
    │ max        ┆ 7.0     ┆ 0.896408 ┆ 2022-12-08 00:00:00.000000 ┆ 2.0   │
    ├╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌┤
    │ median     ┆ 3.5     ┆ 0.42741  ┆ null                       ┆ 1.0   │
    └────────────┴─────────┴──────────┴────────────────────────────┴───────┘

Additional information

- Link to aggregations on `DataFrames` in the Reference guide: [link](https://pola-rs.github.io/polars/py-polars/html/reference/dataframe/aggregation.html)
- Link to descriptive `DataFrame` functions in the Reference guide: [link](https://pola-rs.github.io/polars/py-polars/html/reference/dataframe/descriptive.html)
- Link to `DataFrame` attributes in the Reference guide: [link](https://pola-rs.github.io/polars/py-polars/html/reference/dataframe/attributes.html)

## Expressions

`Expressions` are the core strenght of `Polars`. The `expressions` offer a versatile structure that solves easy queries, but is easily extended to complex analyses. Below we will cover the basic components that serve as building block for all your queries.

- `select`
- `filter`
- `with_columns`

### Select statement

To select a column we need to do two things. Define the `DataFrame` we want the data from. And second, select the data that we need. In the example below you see that we select `col('*')`. The asteriks stands for all columns.

```python
df.select(
    pl.col('*')
)
```

    shape: (8, 4)
    ┌─────┬──────────┬─────────────────────┬───────┐
    │ a   ┆ b        ┆ c                   ┆ d     │
    │ --- ┆ ---      ┆ ---                 ┆ ---   │
    │ i64 ┆ f64      ┆ datetime[μs]        ┆ f64   │
    ╞═════╪══════════╪═════════════════════╪═══════╡
    │ 0   ┆ 0.164545 ┆ 2022-12-01 00:00:00 ┆ 1.0   │
    ├╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌┤
    │ 1   ┆ 0.747291 ┆ 2022-12-02 00:00:00 ┆ 2.0   │
    ├╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌┤
    │ 2   ┆ 0.889227 ┆ 2022-12-03 00:00:00 ┆ NaN   │
    ├╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌┤
    │ 3   ┆ 0.736651 ┆ 2022-12-04 00:00:00 ┆ NaN   │
    ├╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌┤
    │ 4   ┆ 0.099687 ┆ 2022-12-05 00:00:00 ┆ 0.0   │
    ├╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌┤
    │ 5   ┆ 0.965809 ┆ 2022-12-06 00:00:00 ┆ -5.0  │
    ├╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌┤
    │ 6   ┆ 0.93697  ┆ 2022-12-07 00:00:00 ┆ -42.0 │
    ├╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌┤
    │ 7   ┆ 0.848925 ┆ 2022-12-08 00:00:00 ┆ null  │
    └─────┴──────────┴─────────────────────┴───────┘

You can also specify the specific columns that you want to return. There are two ways to do this. The first option is to create a `list` of column names, as seen below.

```python
df.select(
    pl.col(['a', 'b'])
)
```

    shape: (8, 2)
    ┌─────┬──────────┐
    │ a   ┆ b        │
    │ --- ┆ ---      │
    │ i64 ┆ f64      │
    ╞═════╪══════════╡
    │ 0   ┆ 0.164545 │
    ├╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┤
    │ 1   ┆ 0.747291 │
    ├╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┤
    │ 2   ┆ 0.889227 │
    ├╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┤
    │ 3   ┆ 0.736651 │
    ├╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┤
    │ 4   ┆ 0.099687 │
    ├╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┤
    │ 5   ┆ 0.965809 │
    ├╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┤
    │ 6   ┆ 0.93697  │
    ├╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┤
    │ 7   ┆ 0.848925 │
    └─────┴──────────┘

The second option is to specify each column within a `list` in the `select` statement. This option is shown below.

```python
# in this example we limit the number of rows returned to 3, as the comparison is clear.
# this also shows how easy we can extend our expression to what we need. 
df.select([
    pl.col('a'),
    pl.col('b')
]).limit(3)
```

    shape: (3, 2)
    ┌─────┬──────────┐
    │ a   ┆ b        │
    │ --- ┆ ---      │
    │ i64 ┆ f64      │
    ╞═════╪══════════╡
    │ 0   ┆ 0.164545 │
    ├╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┤
    │ 1   ┆ 0.747291 │
    ├╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┤
    │ 2   ┆ 0.889227 │
    └─────┴──────────┘

If you want to exclude an entire column from your view, you can simply use `exclude` in your `select` statement.

```python
df.select([
    pl.exclude('a')
])
```

    shape: (8, 3)
    ┌──────────┬─────────────────────┬───────┐
    │ b        ┆ c                   ┆ d     │
    │ ---      ┆ ---                 ┆ ---   │
    │ f64      ┆ datetime[μs]        ┆ f64   │
    ╞══════════╪═════════════════════╪═══════╡
    │ 0.220182 ┆ 2022-12-01 00:00:00 ┆ 1.0   │
    ├╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌┤
    │ 0.750839 ┆ 2022-12-02 00:00:00 ┆ 2.0   │
    ├╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌┤
    │ 0.634639 ┆ 2022-12-03 00:00:00 ┆ NaN   │
    ├╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌┤
    │ 0.67404  ┆ 2022-12-04 00:00:00 ┆ NaN   │
    ├╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌┤
    │ 0.102818 ┆ 2022-12-05 00:00:00 ┆ 0.0   │
    ├╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌┤
    │ 0.896408 ┆ 2022-12-06 00:00:00 ┆ -5.0  │
    ├╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌┤
    │ 0.062943 ┆ 2022-12-07 00:00:00 ┆ -42.0 │
    ├╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌┤
    │ 0.108093 ┆ 2022-12-08 00:00:00 ┆ null  │
    └──────────┴─────────────────────┴───────┘

Additional information

- Link to `select` with `expressions` in the Polars Book: [link](../dsl/expressions.md)

### Filter

The `filter` option allows us to create a subset of the `DataFrame`. We use the same `DataFrame` as earlier and we filter between two specified dates.

```python
df.filter(
    pl.col("c").is_between(datetime(2022, 12, 2), datetime(2022, 12, 8)),
)
```

    shape: (5, 4)
    ┌─────┬──────────┬─────────────────────┬───────┐
    │ a   ┆ b        ┆ c                   ┆ d     │
    │ --- ┆ ---      ┆ ---                 ┆ ---   │
    │ i64 ┆ f64      ┆ datetime[μs]        ┆ f64   │
    ╞═════╪══════════╪═════════════════════╪═══════╡
    │ 2   ┆ 0.634639 ┆ 2022-12-03 00:00:00 ┆ NaN   │
    ├╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌┤
    │ 3   ┆ 0.67404  ┆ 2022-12-04 00:00:00 ┆ NaN   │
    ├╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌┤
    │ 4   ┆ 0.102818 ┆ 2022-12-05 00:00:00 ┆ 0.0   │
    ├╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌┤
    │ 5   ┆ 0.896408 ┆ 2022-12-06 00:00:00 ┆ -5.0  │
    ├╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌┤
    │ 6   ┆ 0.062943 ┆ 2022-12-07 00:00:00 ┆ -42.0 │
    └─────┴──────────┴─────────────────────┴───────┘

With `filter` you can also create more complex filters that include multiple columns.

```python
df.filter(
    (pl.col('a') <= 3) & (pl.col('d').is_not_nan())
)
```

    shape: (2, 4)
    ┌─────┬──────────┬─────────────────────┬─────┐
    │ a   ┆ b        ┆ c                   ┆ d   │
    │ --- ┆ ---      ┆ ---                 ┆ --- │
    │ i64 ┆ f64      ┆ datetime[μs]        ┆ f64 │
    ╞═════╪══════════╪═════════════════════╪═════╡
    │ 0   ┆ 0.220182 ┆ 2022-12-01 00:00:00 ┆ 1.0 │
    ├╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌┤
    │ 1   ┆ 0.750839 ┆ 2022-12-02 00:00:00 ┆ 2.0 │
    └─────┴──────────┴─────────────────────┴─────┘

Additional information

- Link to filtering in `expressions` in the Polars Book: [link](../dsl/expressions.md#filter-and-conditionals)

### With_columns

`with_colums` allows you to create new columns for you analyses. We create to new columns `e` and `b+42`. First we sum all values from column `b` and store the results in column `e`. After that we add `42` to the values of `b`. Creating a new column `b+42` to store these results.

```python
df.with_columns([
    pl.col('b').sum().alias('e'),
    (pl.col('b') + 42).alias('b+42')
])
```

    shape: (8, 6)
    ┌─────┬──────────┬─────────────────────┬───────┬──────────┬───────────┐
    │ a   ┆ b        ┆ c                   ┆ d     ┆ e        ┆ b+42      │
    │ --- ┆ ---      ┆ ---                 ┆ ---   ┆ ---      ┆ ---       │
    │ i64 ┆ f64      ┆ datetime[μs]        ┆ f64   ┆ f64      ┆ f64       │
    ╞═════╪══════════╪═════════════════════╪═══════╪══════════╪═══════════╡
    │ 0   ┆ 0.606396 ┆ 2022-12-01 00:00:00 ┆ 1.0   ┆ 4.126554 ┆ 42.606396 │
    ├╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌┤
    │ 1   ┆ 0.404966 ┆ 2022-12-02 00:00:00 ┆ 2.0   ┆ 4.126554 ┆ 42.404966 │
    ├╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌┤
    │ 2   ┆ 0.619193 ┆ 2022-12-03 00:00:00 ┆ NaN   ┆ 4.126554 ┆ 42.619193 │
    ├╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌┤
    │ 3   ┆ 0.41586  ┆ 2022-12-04 00:00:00 ┆ NaN   ┆ 4.126554 ┆ 42.41586  │
    ├╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌┤
    │ 4   ┆ 0.35721  ┆ 2022-12-05 00:00:00 ┆ 0.0   ┆ 4.126554 ┆ 42.35721  │
    ├╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌┤
    │ 5   ┆ 0.726861 ┆ 2022-12-06 00:00:00 ┆ -5.0  ┆ 4.126554 ┆ 42.726861 │
    ├╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌┤
    │ 6   ┆ 0.201782 ┆ 2022-12-07 00:00:00 ┆ -42.0 ┆ 4.126554 ┆ 42.201782 │
    ├╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌┤
    │ 7   ┆ 0.794286 ┆ 2022-12-08 00:00:00 ┆ null  ┆ 4.126554 ┆ 42.794286 │
    └─────┴──────────┴─────────────────────┴───────┴──────────┴───────────┘

### Groupby

We will create a new `DataFrame` for the Groupby functionality. This new `DataFrame` will include several 'groups' that we want to groupby.

```python
df2 = pl.DataFrame({
                    "x": np.arange(0, 8), 
                    "y": ['A', 'A', 'A', 'B', 'B', 'C', 'X', 'X'],
})

print(df2)
```

    shape: (8, 2)
    ┌─────┬─────┐
    │ x   ┆ y   │
    │ --- ┆ --- │
    │ i64 ┆ str │
    ╞═════╪═════╡
    │ 0   ┆ A   │
    ├╌╌╌╌╌┼╌╌╌╌╌┤
    │ 1   ┆ A   │
    ├╌╌╌╌╌┼╌╌╌╌╌┤
    │ 2   ┆ A   │
    ├╌╌╌╌╌┼╌╌╌╌╌┤
    │ 3   ┆ B   │
    ├╌╌╌╌╌┼╌╌╌╌╌┤
    │ 4   ┆ B   │
    ├╌╌╌╌╌┼╌╌╌╌╌┤
    │ 5   ┆ C   │
    ├╌╌╌╌╌┼╌╌╌╌╌┤
    │ 6   ┆ X   │
    ├╌╌╌╌╌┼╌╌╌╌╌┤
    │ 7   ┆ X   │
    └─────┴─────┘

```python
# without maintain_order you will get a random order back.
df2.groupby("y", maintain_order=True).count()
```

    shape: (4, 2)
    ┌─────┬───────┐
    │ y   ┆ count │
    │ --- ┆ ---   │
    │ str ┆ u32   │
    ╞═════╪═══════╡
    │ A   ┆ 3     │
    ├╌╌╌╌╌┼╌╌╌╌╌╌╌┤
    │ B   ┆ 2     │
    ├╌╌╌╌╌┼╌╌╌╌╌╌╌┤
    │ C   ┆ 1     │
    ├╌╌╌╌╌┼╌╌╌╌╌╌╌┤
    │ X   ┆ 2     │
    └─────┴───────┘

```python
df2.groupby("y", maintain_order=True).agg([
    pl.col("*").count().alias("count"),
    pl.col("*").sum().alias("sum")
])
```

    shape: (4, 3)
    ┌─────┬───────┬─────┐
    │ y   ┆ count ┆ sum │
    │ --- ┆ ---   ┆ --- │
    │ str ┆ u32   ┆ i64 │
    ╞═════╪═══════╪═════╡
    │ A   ┆ 3     ┆ 3   │
    ├╌╌╌╌╌┼╌╌╌╌╌╌╌┼╌╌╌╌╌┤
    │ B   ┆ 2     ┆ 7   │
    ├╌╌╌╌╌┼╌╌╌╌╌╌╌┼╌╌╌╌╌┤
    │ C   ┆ 1     ┆ 5   │
    ├╌╌╌╌╌┼╌╌╌╌╌╌╌┼╌╌╌╌╌┤
    │ X   ┆ 2     ┆ 13  │
    └─────┴───────┴─────┘

Additional information

- Link to `groupby` with `expressions` in the Polars Book: [link](../dsl/groupby.md)

### Combining operations

Below are some examples on how to combine operations to create the `DataFrame` you require.

```python
# create a new colum that multiplies column `a` and `b` from our DataFrame
# select all the columns, but exclude column `c` and `d` from the final DataFrame

df_x = df.with_column(
    (pl.col("a") * pl.col("b")).alias("a * b")
).select([
    pl.all().exclude(['c', 'd'])
])

print(df_x)
```

    shape: (8, 3)
    ┌─────┬──────────┬──────────┐
    │ a   ┆ b        ┆ a * b    │
    │ --- ┆ ---      ┆ ---      │
    │ i64 ┆ f64      ┆ f64      │
    ╞═════╪══════════╪══════════╡
    │ 0   ┆ 0.220182 ┆ 0.0      │
    ├╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┤
    │ 1   ┆ 0.750839 ┆ 0.750839 │
    ├╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┤
    │ 2   ┆ 0.634639 ┆ 1.269277 │
    ├╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┤
    │ 3   ┆ 0.67404  ┆ 2.022121 │
    ├╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┤
    │ 4   ┆ 0.102818 ┆ 0.41127  │
    ├╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┤
    │ 5   ┆ 0.896408 ┆ 4.482038 │
    ├╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┤
    │ 6   ┆ 0.062943 ┆ 0.377657 │
    ├╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┤
    │ 7   ┆ 0.108093 ┆ 0.756653 │
    └─────┴──────────┴──────────┘

```python
# only excluding column `d` in this example

df_y = df.with_columns([
    (pl.col("a") * pl.col("b")).alias("a * b")
]).select([
    pl.all().exclude('d')
])

print(df_y)
```

    shape: (8, 4)
    ┌─────┬──────────┬─────────────────────┬──────────┐
    │ a   ┆ b        ┆ c                   ┆ a * b    │
    │ --- ┆ ---      ┆ ---                 ┆ ---      │
    │ i64 ┆ f64      ┆ datetime[μs]        ┆ f64      │
    ╞═════╪══════════╪═════════════════════╪══════════╡
    │ 0   ┆ 0.220182 ┆ 2022-12-01 00:00:00 ┆ 0.0      │
    ├╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┤
    │ 1   ┆ 0.750839 ┆ 2022-12-02 00:00:00 ┆ 0.750839 │
    ├╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┤
    │ 2   ┆ 0.634639 ┆ 2022-12-03 00:00:00 ┆ 1.269277 │
    ├╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┤
    │ 3   ┆ 0.67404  ┆ 2022-12-04 00:00:00 ┆ 2.022121 │
    ├╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┤
    │ 4   ┆ 0.102818 ┆ 2022-12-05 00:00:00 ┆ 0.41127  │
    ├╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┤
    │ 5   ┆ 0.896408 ┆ 2022-12-06 00:00:00 ┆ 4.482038 │
    ├╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┤
    │ 6   ┆ 0.062943 ┆ 2022-12-07 00:00:00 ┆ 0.377657 │
    ├╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┤
    │ 7   ┆ 0.108093 ┆ 2022-12-08 00:00:00 ┆ 0.756653 │
    └─────┴──────────┴─────────────────────┴──────────┘

Additional information

- Link to contexts in `expressions` in the Polars Book: [link](../dsl/contexts.md)

## Combining dataframes

### Join

Let's have a closer look on how to `join` two `DataFrames` to a single `DataFrame`.

```python
df = pl.DataFrame({"a": np.arange(0, 8), 
                   "b": np.random.rand(8), 
                   "c": [datetime(2022, 12, 1) + timedelta(days=idx) for idx in range(8)],
                   "d": [1, 2.0, np.NaN, np.NaN, 0, -5, -42, None]
                  })

df2 = pl.DataFrame({
                    "x": np.arange(0, 8), 
                    "y": ['A', 'A', 'A', 'B', 'B', 'C', 'X', 'X'],
})
```

Our two `DataFrames` both have an 'id'-like column: `a` and `x`. We can use those columns to `join` the `DataFrames` in this example.

```python
df.join(df2, left_on="a", right_on="x")
```

    shape: (8, 5)
    ┌─────┬──────────┬─────────────────────┬───────┬─────┐
    │ a   ┆ b        ┆ c                   ┆ d     ┆ y   │
    │ --- ┆ ---      ┆ ---                 ┆ ---   ┆ --- │
    │ i64 ┆ f64      ┆ datetime[μs]        ┆ f64   ┆ str │
    ╞═════╪══════════╪═════════════════════╪═══════╪═════╡
    │ 0   ┆ 0.220182 ┆ 2022-12-01 00:00:00 ┆ 1.0   ┆ A   │
    ├╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌┼╌╌╌╌╌┤
    │ 1   ┆ 0.750839 ┆ 2022-12-02 00:00:00 ┆ 2.0   ┆ A   │
    ├╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌┼╌╌╌╌╌┤
    │ 2   ┆ 0.634639 ┆ 2022-12-03 00:00:00 ┆ NaN   ┆ A   │
    ├╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌┼╌╌╌╌╌┤
    │ 3   ┆ 0.67404  ┆ 2022-12-04 00:00:00 ┆ NaN   ┆ B   │
    ├╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌┼╌╌╌╌╌┤
    │ 4   ┆ 0.102818 ┆ 2022-12-05 00:00:00 ┆ 0.0   ┆ B   │
    ├╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌┼╌╌╌╌╌┤
    │ 5   ┆ 0.896408 ┆ 2022-12-06 00:00:00 ┆ -5.0  ┆ C   │
    ├╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌┼╌╌╌╌╌┤
    │ 6   ┆ 0.062943 ┆ 2022-12-07 00:00:00 ┆ -42.0 ┆ X   │
    ├╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌┼╌╌╌╌╌┤
    │ 7   ┆ 0.108093 ┆ 2022-12-08 00:00:00 ┆ null  ┆ X   │
    └─────┴──────────┴─────────────────────┴───────┴─────┘

Additional information

- Link to `joins` in the Polars Book: [link](../howcani/combining_data/joining.md)
- More information about `joins` in the Reference guide [link](https://pola-rs.github.io/polars/py-polars/html/reference/dataframe/api/polars.DataFrame.join.html#polars.DataFrame.join)

### Concat

We can also `concatenate` two `DataFrames`. Vertical concatenation will make the `DataFrame` longer. Horizontal concatenation will make the `DataFrame` wider. Below you can see the result of an horizontal concatenation of our two `DataFrames`.

```python
pl.concat([df,df2], how="horizontal")
```

    shape: (8, 6)
    ┌─────┬──────────┬─────────────────────┬───────┬─────┬─────┐
    │ a   ┆ b        ┆ c                   ┆ d     ┆ x   ┆ y   │
    │ --- ┆ ---      ┆ ---                 ┆ ---   ┆ --- ┆ --- │
    │ i64 ┆ f64      ┆ datetime[μs]        ┆ f64   ┆ i64 ┆ str │
    ╞═════╪══════════╪═════════════════════╪═══════╪═════╪═════╡
    │ 0   ┆ 0.220182 ┆ 2022-12-01 00:00:00 ┆ 1.0   ┆ 0   ┆ A   │
    ├╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌┼╌╌╌╌╌┼╌╌╌╌╌┤
    │ 1   ┆ 0.750839 ┆ 2022-12-02 00:00:00 ┆ 2.0   ┆ 1   ┆ A   │
    ├╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌┼╌╌╌╌╌┼╌╌╌╌╌┤
    │ 2   ┆ 0.634639 ┆ 2022-12-03 00:00:00 ┆ NaN   ┆ 2   ┆ A   │
    ├╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌┼╌╌╌╌╌┼╌╌╌╌╌┤
    │ 3   ┆ 0.67404  ┆ 2022-12-04 00:00:00 ┆ NaN   ┆ 3   ┆ B   │
    ├╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌┼╌╌╌╌╌┼╌╌╌╌╌┤
    │ 4   ┆ 0.102818 ┆ 2022-12-05 00:00:00 ┆ 0.0   ┆ 4   ┆ B   │
    ├╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌┼╌╌╌╌╌┼╌╌╌╌╌┤
    │ 5   ┆ 0.896408 ┆ 2022-12-06 00:00:00 ┆ -5.0  ┆ 5   ┆ C   │
    ├╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌┼╌╌╌╌╌┼╌╌╌╌╌┤
    │ 6   ┆ 0.062943 ┆ 2022-12-07 00:00:00 ┆ -42.0 ┆ 6   ┆ X   │
    ├╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌┼╌╌╌╌╌┼╌╌╌╌╌┤
    │ 7   ┆ 0.108093 ┆ 2022-12-08 00:00:00 ┆ null  ┆ 7   ┆ X   │
    └─────┴──────────┴─────────────────────┴───────┴─────┴─────┘

Additional information

- Link to `concatenation` in the Polars Book: [link](../howcani/combining_data/concatenating.md)
- More information about `concatenation` in the Reference guide [link](https://pola-rs.github.io/polars/py-polars/html/reference/api/polars.concat.html#polars.concat)

## Remaining topics

This guide was a quick introduction to some of the most used functions within `Polars`. There is a lot more to explore, both in the Polars Book as in the Reference guide. Below are other common topics including a link to find more information about them.

- Dealing with timeseries [link](../howcani/timeseries/intro.md)
- Processing missing data [link](../howcani/missing_data.md)
- Reading data from Pandas DataFrame or Numpy array [link](https://pola-rs.github.io/polars/py-polars/html/reference/functions.html#conversion)
- Working with the Lazy API [link](../optimizations/)
