# Missing data
Each column in a `Polars` dataframe is an Arrow array based on the Apache Arrow format.
Handling missing data in a sensible manner was one of the goals of the Apache Arrow project.

## `null` and `NaN` values
Missing data is represented in Arrow and `Polars` with a `null` value. This `null` missing value applies for all data types including numerical values. `Polars` also allows `NotaNumber` or `NaN` values for float columns. These `NaN` values are considered to be a type of floating point data rather than missing data. We discuss `NaN` values separately below.

You can manually define a missing value with the python `None` value:

```python
{{#include examples/missing_data/missing_types.py:4:4}}
print(df)
```

```text
{{#include outputs/missing_data/none_missing_value_df.txt}}
```

## Missing data metadata
The Arrow arrays used by `Polars` for a `Series` or a column in a `DataFrame` store metadata related to missing data.

Firstly, there is the `null_count` that is the number of rows with `null` values in the column. 

Secondly, if the `null_count` is greater than 0 there is a validity bitmap. The validity bitmap is an array that tells you whether each value is present or missing.

You can access the `null_count` for a `Series` or a `DataFrame` with the `null_count` method: 
```python
{{#include examples/missing_data/missing_types.py:6:6}}
print(nullCountDf)
```

```text
{{#include outputs/missing_data/null_count_df.txt}}
```
Although `null_count` is a method in python-polars this is a cheap operation as `null_count` is already calculated for the Arrow array.

You can access a `Series` based on the validity bitmap with the `is_null` method:

```python
{{#include examples/missing_data/missing_types.py:8:8}}
print(isNullSeries)
```

```text
{{#include outputs/missing_data/isnull_series.txt}}
```
As for `null_count` the `is_null` method is a cheap operation as the validity bitmap is already calculated for the Arrow array.

## Filling missing data
Missing data in a `Series` can be filled with the `fill_null` method. You have to specify how you want the `fill_null` method to fill the missing data. The three main ways to do this are with:
- a literal such as 0 or "0"
- a strategy such as filling forwards or interpolation
- an expression such as replacing with values from another column

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
We can fill the missing data with a strategy:
```python
{{#include examples/missing_data/fill_strategies.py:7:7}}
print(fillForward)
```

```text
{{#include outputs/missing_data/fill_strategies_forward_df.txt}}
```
See the [API docs](https://pola-rs.github.io/polars/py-polars/html/reference/api/polars.Series.fill_null.html) for other strategies available.

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
In addition, we can fill nulls with interpolation without using the `fill_null` function:

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
However, if you try to include a `NaN` value in an integer column it will raise an exception.


`NaN` values are considered to be a type of floating point data and are **not** considered missing data in `Polars`. This means: 
- `NaN` values are **not** counted with the `null_count` method
- `NaN` values are filled when you use `fill_nan` method but are **not** filled with the `fill_null` method
