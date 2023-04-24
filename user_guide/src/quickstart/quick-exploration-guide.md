# Polars quick exploration guide

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
{{#include ../examples/quickstart/series_tuple.py:3:}}

print(series)
```

```text
{{#include ../outputs/quickstart/series_list.txt}}
```

```python
{{#include ../examples/quickstart/series_list.py:3:}}

print(series)
```

```text
{{#include ../outputs/quickstart/series_list.txt}}
```

A `DataFrame` is created from a `dict` or a collection of `dicts`.

```python
{{#include ../examples/quickstart/dataframe1.py:4:}}

print(df)
```

```text
{{#include ../outputs/quickstart/output.csv}}
```

Additional information

- Link to `Series` in the Reference guide: [link](POLARS_PY_REF_GUIDE/series/index.html)
- Link to `DataFrames` in the Reference guide: [link](POLARS_PY_REF_GUIDE/dataframe/index.html)

### From files

In Polars we can also read files and create a `DataFrame`. In the following examples we write the output of the `DataFrame` from the previous part to a specific file type (`csv`, `json` and `parquet`). After that we will read it and print the output for inspection.

#### csv

```python
dataframe.write_csv('output.csv')
```

```python
{{#include ../examples/quickstart/read_csv_datetime.py:3:}}

print(df_csv_with_dates)
```

```text
{{#include ../outputs/quickstart/output.csv}}
```

You can add `try_parse_dates=True` to ensure that date column(s) are set as datetime.

#### json

```python
dataframe.write_json('output.json')
```

```python
{{#include ../examples/quickstart/read_json.py:3:}}

print(df_json)
```

```text
{{#include ../outputs/quickstart/output.json}}
```

#### parquet

```python
dataframe.write_parquet('output.parquet')
```

```python
{{#include ../examples/quickstart/read_parquet.py:3:}}

print(df_parquet)
```

```text
{{#include ../outputs/quickstart/output.parquet}}
```

Additional information

- Read more about `IO` in the Polars Book: [link](../howcani/io/intro.html)
- Link to `IO` in the Reference guide: [link](POLARS_PY_REF_GUIDE/io.html)

## Viewing data

This part focuses on viewing data in a `DataFrame`. We first create a `DataFrame` to work with.

```python
{{#include ../examples/quickstart/dataframe2.py:5:}}

print(df)
```

```text
{{#include ../outputs/quickstart/output2.csv}}
```

The `head` function shows by default the first 5 rows of a `DataFrame`. You can specify the number of rows you want to see (e.g. `df.head(10)`).

```python
{{#include ../examples/quickstart/head.py:3:}}

print(out)
```

```text
{{#include ../outputs/quickstart/head.txt}}
```

The `tail` function shows the last 5 rows of a `DataFrame`. You can also specify the number of rows you want to see, similar to `head`.

```python
{{#include ../examples/quickstart/tail.py:3:}}

print(out)
```

```text
{{#include ../outputs/quickstart/tail.txt}}
```

If you want to get an impression of the data of your `DataFrame`, you can also use `sample`. With `sample` you get an *n* number of random rows from the `DataFrame`.

```python
{{#include ../examples/quickstart/sample.py:3:}}

print(out)
```

```text
{{#include ../outputs/quickstart/sample.txt}}
```

`Describe` returns summary statistics of your `DataFrame`. It will provide several quick statistics if possible.

```python
{{#include ../examples/quickstart/describe.py:3:}}

print(out)
```

```text
{{#include ../outputs/quickstart/describe.txt}}
```

Additional information

- Link to aggregations on `DataFrames` in the Reference guide: [link](POLARS_PY_REF_GUIDE/dataframe/aggregation.html)
- Link to descriptive `DataFrame` functions in the Reference guide: [link](POLARS_PY_REF_GUIDE/dataframe/descriptive.html)
- Link to `DataFrame` attributes in the Reference guide: [link](POLARS_PY_REF_GUIDE/dataframe/attributes.html)

## Expressions

`Expressions` are the core strength of `Polars`. The `expressions` offer a versatile structure that solves easy queries, but is easily extended to complex analyses. Below we will cover the basic components that serve as building block for all your queries.

- `select`
- `filter`
- `with_columns`

### Select statement

To select a column we need to do two things. Define the `DataFrame` we want the data from. And second, select the data that we need. In the example below you see that we select `col('*')`. The asterisk stands for all columns.

```python
{{#include ../examples/quickstart/select1.py:4:}}

print(out)
```

```text
{{#include ../outputs/quickstart/select1.txt}}
```

You can also specify the specific columns that you want to return. There are two ways to do this. The first option is to create a `list` of column names, as seen below.

```python
{{#include ../examples/quickstart/select2.py:4:}}

print(out)
```

```text
{{#include ../outputs/quickstart/select2.txt}}
```

The second option is to specify each column within a `list` in the `select` statement. This option is shown below.

```python
{{#include ../examples/quickstart/select3.py:4:}}

print(out)
```

```text
{{#include ../outputs/quickstart/select3.txt}}
```

If you want to exclude an entire column from your view, you can simply use `exclude` in your `select` statement.

```python
{{#include ../examples/quickstart/select4.py:4:}}

print(out)
```

```text
{{#include ../outputs/quickstart/select4.txt}}
```

Additional information

- Link to `select` with `expressions` in the Polars Book: [link](../dsl/expressions.md)

### Filter

The `filter` option allows us to create a subset of the `DataFrame`. We use the same `DataFrame` as earlier and we filter between two specified dates.

```python
{{#include ../examples/quickstart/filter1.py:5:}}

print(out)
```

```text
{{#include ../outputs/quickstart/filter1.txt}}
```

With `filter` you can also create more complex filters that include multiple columns.

```python
{{#include ../examples/quickstart/filter2.py:4:}}

print(out)
```

```text
{{#include ../outputs/quickstart/filter2.txt}}
```

Additional information

- Link to filtering in `expressions` in the Polars Book: [link](../dsl/expressions.md#filter-and-conditionals)

### With_columns

`with_columns` allows you to create new columns for you analyses. We create two new columns `e` and `b+42`. First we sum all values from column `b` and store the results in column `e`. After that we add `42` to the values of `b`. Creating a new column `b+42` to store these results.

```python
{{#include ../examples/quickstart/withcolumns.py:4:}}

print(out)
```

```text
{{#include ../outputs/quickstart/withcolumns.txt}}
```

### Groupby

We will create a new `DataFrame` for the Groupby functionality. This new `DataFrame` will include several 'groups' that we want to groupby.

```python
{{#include ../examples/quickstart/dataframe3.py}}

print(df)
```

```text
{{#include ../outputs/quickstart/output3.csv}}
```

```python
# without maintain_order you will get a random order back.
{{#include ../examples/quickstart/groupby1.py:4:}}

print(out)
```

```text
{{#include ../outputs/quickstart/groupby1.txt}}
```

```python
{{#include ../examples/quickstart/groupby2.py:4:}}

print(out)
```

```text
{{#include ../outputs/quickstart/groupby2.txt}}
```

Additional information

- Link to `groupby` with `expressions` in the Polars Book: [link](../dsl/groupby.md)

### Combining operations

Below are some examples on how to combine operations to create the `DataFrame` you require.

```python
# create a new column that multiplies column `a` and `b` from our DataFrame
# select all the columns, but exclude column `c` and `d` from the final DataFrame

{{#include ../examples/quickstart/combine1.py:4:}}

print(out)
```

```text
{{#include ../outputs/quickstart/combine1.txt}}
```

```python
# only excluding column `d` in this example

{{#include ../examples/quickstart/combine2.py:4:}}

print(out)
```

```text
{{#include ../outputs/quickstart/combine2.txt}}
```

Additional information

- Link to contexts in `expressions` in the Polars Book: [link](../dsl/contexts.md)

## Combining dataframes

### Join

Let's have a closer look on how to `join` two `DataFrames` to a single `DataFrame`.

```python
{{#include ../examples/quickstart/join_df1.py:4:}}

{{#include ../examples/quickstart/join_df2.py:3:}}
```

Our two `DataFrames` both have an 'id'-like column: `a` and `x`. We can use those columns to `join` the `DataFrames` in this example.

```python
{{#include ../examples/quickstart/qs_join1.py:5:}}

print(out)
```

```text
{{#include ../outputs/quickstart/qs_join1.txt}}
```

Additional information

- Link to `joins` in the Polars Book: [link](../howcani/combining_data/joining.md)
- More information about `joins` in the Reference guide [link](POLARS_PY_REF_GUIDE/dataframe/api/polars.DataFrame.join.html#polars.DataFrame.join)

### Concat

We can also `concatenate` two `DataFrames`. Vertical concatenation will make the `DataFrame` longer. Horizontal concatenation will make the `DataFrame` wider. Below you can see the result of an horizontal concatenation of our two `DataFrames`.

```python
{{#include ../examples/quickstart/concat1.py:5:}}

print(out)
```

```text
{{#include ../outputs/quickstart/concat1.txt}}
```

Additional information

- Link to `concatenation` in the Polars Book: [link](../howcani/combining_data/concatenating.md)
- More information about `concatenation` in the Reference guide [link](POLARS_PY_REF_GUIDE/api/polars.concat.html#polars.concat)

## Remaining topics

This guide was a quick introduction to some of the most used functions within `Polars`. There is a lot more to explore, both in the Polars Book as in the Reference guide. Below are other common topics including a link to find more information about them.

- Dealing with timeseries [link](../howcani/timeseries/intro.md)
- Processing missing data [link](../howcani/missing_data.md)
- Reading data from Pandas DataFrame or Numpy array [link](POLARS_PY_REF_GUIDE/functions.html#conversion)
- Working with the Lazy API [link](../optimizations/)
