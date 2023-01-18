# Missing data

This page sets out how missing data is represented in `Polars` and how missing data can be filled.

## `null` and `NaN` values

Each column in a `DataFrame` (or equivalently a `Series`) is an Arrow array or a collection of Arrow arrays [based on the Apache Arrow format](https://arrow.apache.org/docs/format/Columnar.html#null-count). Missing data is represented in Arrow and `Polars` with a `null` value. This `null` missing value applies for all data types including numerical values.

`Polars` also allows `NotaNumber` or `NaN` values for float columns. These `NaN` values are considered to be a type of floating point data rather than missing data. We discuss `NaN` values separately below.

You can manually define a missing value with the python `None` value:

```python
{{#include ../examples/missing_data/missing_types.py:4:8}}
print(df)
```

```text
{{#include ../outputs/missing_data/none_missing_value_df.txt}}
```

> In `Pandas` the value for missing data depends on the dtype of the column. In `Polars` missing data is always represented as a `null` value.

## Missing data metadata

Each Arrow array used by `Polars` stores two kinds of metadata related to missing data. This metadata allows `Polars` to quickly show how many missing values there are and which values are missing.

The first piece of metadata is the `null_count` - this is the number of rows with `null` values in the column:

```python
{{#include ../examples/missing_data/missing_types.py:10:10}}
print(null_count_df)
```

```text
{{#include ../outputs/missing_data/null_count_df.txt}}
```

The `null_count` method can be called on a `DataFrame`, a column from a `DataFrame` or a `Series`. The `null_count`method is a cheap operation as `null_count` is already calculated for the underlying Arrow array.

The second piece of metadata is an array called a *validity bitmap* that indicates whether each data value is valid or missing.
The validity bitmap is memory efficient as it is bit encoded - each value is either a 0 or a 1. This bit encoding means the memory overhead per array is only (array length / 8) bytes. The validity bitmap is used by the `is_null` method in `Polars`.

You can return a `Series` based on the validity bitmap for a column in a `DataFrame` or a `Series` with the `is_null` method:

```python
{{#include ../examples/missing_data/missing_types.py:12:14}}
print(is_null_series)
```

```text
{{#include ../outputs/missing_data/isnull_series.txt}}
```

The `is_null` method is a cheap operation that does not require scanning the full column for `null` values. This is because the validity bitmap already exists and can be returned as a Boolean array.

## Filling missing data

Missing data in a `Series` can be filled with the `fill_null` method. You have to specify how you want the `fill_null` method to fill the missing data. The main ways to do this are filling with:

- a literal such as 0 or "0"
- a strategy such as filling forwards
- an expression such as replacing with values from another column
- interpolation

We illustrate each way to fill nulls by defining a simple `DataFrame` with a missing value in `col2`:

```python
{{#include ../examples/missing_data/fill_strategies.py:3:8}}
print(df)
```

```text
{{#include ../outputs/missing_data/fill_strategies_df.txt}}
```

### Fill with specified literal value

We can fill the missing data with a specified literal value with `pl.lit`:

```python
{{#include ../examples/missing_data/fill_strategies.py:10:16}}
print(fill_literal_df)
```

```text
{{#include ../outputs/missing_data/fill_strategies_literal_df.txt}}
```

### Fill with a strategy

We can fill the missing data with a strategy such as filling forward:

```python
{{#include ../examples/missing_data/fill_strategies.py:18:20}}
print(fill_forward_df)
```

```text
{{#include ../outputs/missing_data/fill_strategies_forward_df.txt}}
```

See the [API docs](POLARS_PY_REF_GUIDE/series/api/polars.Series.fill_null.html) for other available strategies.

### Fill with an expression

For more flexibility we can fill the missing data with an expression. For example,
to fill nulls with the median value from that column:

```python
{{#include ../examples/missing_data/fill_strategies.py:22:24}}
print(fill_median_df)
```

```text
{{#include ../outputs/missing_data/fill_strategies_median_df.txt}}
```

In this case the column is cast from integer to float because the median is a float statistic.

### Fill with interpolation

In addition, we can fill nulls with interpolation (without using the `fill_null` function):

```python
{{#include ../examples/missing_data/fill_strategies.py:26:28}}
print(fill_interpolation)
```

```text
{{#include ../outputs/missing_data/fill_strategies_interpolate_df.txt}}
```

## `NotaNumber` or `NaN` values

Missing data in a `Series` has a `null` value. However, you can use `NotaNumber` or `NaN` values in columns with float datatypes. These `NaN` values can be created from Numpy's `np.nan` or the native python `float('nan')`:

```python
{{#include ../examples/missing_data/missing_types.py:16:20}}
print(nan_df)
```

```text
{{#include ../outputs/missing_data/nan_missing_value_df.txt}}
```

> In `Pandas` by default a `NaN` value in an integer column causes the column to be cast to float. This does not happen in `Polars` - instead an exception is raised.

`NaN` values are considered to be a type of floating point data and are **not considered to be missing data** in `Polars`. This means:

- `NaN` values are **not** counted with the `null_count` method
- `NaN` values are filled when you use `fill_nan` method but are **not** filled with the `fill_null` method

`Polars` has `is_nan` and `fill_nan` methods which work in a similar way to the `is_null` and `fill_null` methods. The underlying Arrow arrays do not have a pre-computed validity bitmask for `NaN` values so this has to be computed for the `is_nan` method.

One further difference between `null` and `NaN` values is that taking the `mean` of a column with `null` values excludes the `null` values from the calculation but with `NaN` values taking the mean results in a `NaN`. This behaviour can be avoided by replacing the `NaN` values with `null` values;

```python
{{#include ../examples/missing_data/fill_strategies.py:35:38}}
print(mean_nan_df)
```

```text
{{#include ../outputs/missing_data/fill_strategies_mean_df.txt}}
```
