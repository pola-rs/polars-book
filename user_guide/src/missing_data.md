# Missing data
This page sets out how missing data is represented in `Polars` and how missing data can be filled.

## `null` and `NaN` values
Each `Series` or column in a `DataFrame` is an Arrow array based on the Apache Arrow format. 
Missing data is represented in Arrow and `Polars` with a `null` value. This `null` missing value applies for all data types including numerical values. 

`Polars` also allows `NotaNumber` or `NaN` values for float columns. These `NaN` values are considered to be a type of floating point data rather than missing data. We discuss `NaN` values separately below.

You can manually define a missing value with the python `None` value:

```python
{{#include examples/missing_data/missing_types.py:4:4}}
print(df)
```

```text
{{#include outputs/missing_data/none_missing_value_df.txt}}
```
> In `Pandas` the value for missing data depends on the dtype of the column. In `Polars` missing data is always represented as a `null` value.

## Missing data metadata
The Arrow arrays used by `Polars` for each column in a `DataFrame` store metadata related to missing data.

Firstly, there is the `null_count`: this is the number of rows with `null` values in the column. 

Secondly, if the `null_count` is greater than 0 there is a *validity bitmap*. The validity bitmap is an array that tells you whether each value is present or missing. The validity bitmap is part of the Arrow array for each column.

You can access the `null_count` for a `DataFrame` with the `null_count` method: 
```python
{{#include examples/missing_data/missing_types.py:6:6}}
print(nullCountDf)
```

```text
{{#include outputs/missing_data/null_count_df.txt}}
```
Although `null_count` is a method in python-polars this is a cheap operation as `null_count` is already calculated for the underlying Arrow array for that column.

You can access a `Series` based on the validity bitmap for a column with the `is_null` method:

```python
{{#include examples/missing_data/missing_types.py:8:8}}
print(isNullSeries)
```

```text
{{#include outputs/missing_data/isnull_series.txt}}
```
As for `null_count` the `is_null` method is a cheap operation as the validity bitmap is already calculated for the Arrow array for each column.

## Filling missing data
Missing data in a `Series` can be filled with the `fill_null` method. You have to specify how you want the `fill_null` method to fill the missing data. The main ways to do this are filling with:
- a literal such as 0 or "0"
- a strategy such as filling forwards
- an expression such as replacing with values from another column
- interpolation

We illustrate these by defining a simple `DataFrame` with a missing value in `col2`:
```python
{{#include examples/missing_data/fill_strategies.py:3:3}}
print(df)
```

```text
{{#include outputs/missing_data/fill_strategies_df.txt}}
```
### Fill with specified literal value
We can fill the missing data with a specified literal value with `pl.lit`:
```python
{{#include examples/missing_data/fill_strategies.py:5:5}}
print(fillLiteral)
```

```text
{{#include outputs/missing_data/fill_strategies_literal_df.txt}}
```
### Fill with a strategy
We can fill the missing data with a strategy such as filling forward:
```python
{{#include examples/missing_data/fill_strategies.py:7:7}}
print(fillForward)
```

```text
{{#include outputs/missing_data/fill_strategies_forward_df.txt}}
```
See the [API docs](https://pola-rs.github.io/polars/py-polars/html/reference/api/polars.Series.fill_null.html) for other available strategies.

### Fill with an expression
For more flexibility we can fill the missing data with an expression. For example, 
to fill nulls with the median value from that column:

```python
{{#include examples/missing_data/fill_strategies.py:9:9}}
print(fillMedian)
```

```text
{{#include outputs/missing_data/fill_strategies_median_df.txt}}
```
In this case the column is cast from integer to float because the median is a float statistic.

### Fill with interpolation
In addition, we can fill nulls with interpolation (without using the `fill_null` function):

```python
{{#include examples/missing_data/fill_strategies.py:11:11}}
print(fillInterpolation)
```

```text
{{#include outputs/missing_data/fill_strategies_interpolate_df.txt}}
```


## `NotaNumber` or `NaN` values
Missing data in a `Series` has a `null` value. However, you can use `NotaNumber` or `NaN` values in columns with *float* datatypes. These `NaN` values can be based on Numpy's `np.nan` or the native python `float('nan')`:
```python
{{#include examples/missing_data/missing_types.py:10:10}}
print(dfNaN)
```
```text
{{#include outputs/missing_data/nan_missing_value_df.txt}}
```
However, if you try to include a `NaN` value in an integer column it will raise an exception - only float column can have `NaN` values.

> In `Pandas` a `NaN` value in an integer column causes the column to be cast to float. This does not happen in `Polars` - instead an exception is raised.

`NaN` values are considered to be a type of floating point data and are **not** considered missing data in `Polars`. This means: 
- `NaN` values are **not** counted with the `null_count` method
- `NaN` values are filled when you use `fill_nan` method but are **not** filled with the `fill_null` method

`Polars` has `is_nan` and `fill_nan` methods which work in a similar way to the `is_null` and `fill_null` methods. The main difference is that the underlying Arrow array for a `Series` or a column in a `DataFrame` do not have a pre-computed validity bitmask for `NaN` values so this has to be computed for `is_nan`.

One further difference between `null` and `NaN` values is that taking the `mean` of a column with `null` values excludes the `null` values from the calculation but with `NaN` values taking the mean results in a `NaN`. 

This can be avoided by replacing the `NaN` values with `null` values;
```python
{{#include examples/missing_data/fill_strategies.py:13:14}}
print(meanNaN)
```
```text
{{#include outputs/missing_data/fill_strategies_mean_df.txt}}
```
