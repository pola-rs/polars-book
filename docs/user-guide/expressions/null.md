# Missing data

This page sets out how missing data is represented in `Polars` and how missing data can be filled.

## `null` and `NaN` values

Each column in a `DataFrame` (or equivalently a `Series`) is an Arrow array or a collection of Arrow arrays [based on the Apache Arrow format](https://arrow.apache.org/docs/format/Columnar.html#null-count). Missing data is represented in Arrow and `Polars` with a `null` value. This `null` missing value applies for all data types including numerical values.

`Polars` also allows `NotaNumber` or `NaN` values for float columns. These `NaN` values are considered to be a type of floating point data rather than missing data. We discuss `NaN` values separately below.

You can manually define a missing value with the python `None` value:

=== ":fontawesome-brands-python: Python"
    ``` python
    --8<-- "user-guide/python/expressions/null.py:dataframe"
    ```

```
shape: (2, 1)
┌───────┐
│ value │
│ ---   │
│ i64   │
╞═══════╡
│ 1     │
│ null  │
└───────┘
```

!!! info
    In `Pandas` the value for missing data depends on the dtype of the column. In `Polars` missing data is always represented as a `null` value.

## Missing data metadata

Each Arrow array used by `Polars` stores two kinds of metadata related to missing data. This metadata allows `Polars` to quickly show how many missing values there are and which values are missing.

The first piece of metadata is the `null_count` - this is the number of rows with `null` values in the column:

=== ":fontawesome-brands-python: Python"
    ``` python
    --8<-- "user-guide/python/expressions/null.py:count"
    ```


```text
shape: (1, 1)
┌───────┐
│ value │
│ ---   │
│ u32   │
╞═══════╡
│ 1     │
└───────┘
```

The `null_count` method can be called on a `DataFrame`, a column from a `DataFrame` or a `Series`. The `null_count`method is a cheap operation as `null_count` is already calculated for the underlying Arrow array.

The second piece of metadata is an array called a *validity bitmap* that indicates whether each data value is valid or missing.
The validity bitmap is memory efficient as it is bit encoded - each value is either a 0 or a 1. This bit encoding means the memory overhead per array is only (array length / 8) bytes. The validity bitmap is used by the `is_null` method in `Polars`.

You can return a `Series` based on the validity bitmap for a column in a `DataFrame` or a `Series` with the `is_null` method:

=== ":fontawesome-brands-python: Python"
    ``` python
    --8<-- "user-guide/python/expressions/null.py:isnull"
    ```


```text
shape: (2, 1)
┌───────┐
│ value │
│ ---   │
│ bool  │
╞═══════╡
│ false │
│ true  │
└───────┘
```

The `is_null` method is a cheap operation that does not require scanning the full column for `null` values. This is because the validity bitmap already exists and can be returned as a Boolean array.

## Filling missing data

Missing data in a `Series` can be filled with the `fill_null` method. You have to specify how you want the `fill_null` method to fill the missing data. The main ways to do this are filling with:

- a literal such as 0 or "0"
- a strategy such as filling forwards
- an expression such as replacing with values from another column
- interpolation

We illustrate each way to fill nulls by defining a simple `DataFrame` with a missing value in `col2`:

=== ":fontawesome-brands-python: Python"
    ``` python
    --8<-- "user-guide/python/expressions/null.py:dataframe2"
    ```


```text
shape: (3, 2)
┌──────┬──────┐
│ col1 ┆ col2 │
│ ---  ┆ ---  │
│ i64  ┆ i64  │
╞══════╪══════╡
│ 1    ┆ 1    │
│ 2    ┆ null │
│ 3    ┆ 3    │
└──────┴──────┘
```

### Fill with specified literal value

We can fill the missing data with a specified literal value with `pl.lit`:

=== ":fontawesome-brands-python: Python"
    ``` python
    --8<-- "user-guide/python/expressions/null.py:fill"
    ```


```text
shape: (3, 2)
┌──────┬──────┐
│ col1 ┆ col2 │
│ ---  ┆ ---  │
│ i64  ┆ i64  │
╞══════╪══════╡
│ 1    ┆ 1    │
│ 2    ┆ 2    │
│ 3    ┆ 3    │
└──────┴──────┘
```

### Fill with a strategy

We can fill the missing data with a strategy such as filling forward:

=== ":fontawesome-brands-python: Python"
    ``` python
    --8<-- "user-guide/python/expressions/null.py:fillstrategy"
    ```


```text
shape: (3, 2)
┌──────┬──────┐
│ col1 ┆ col2 │
│ ---  ┆ ---  │
│ i64  ┆ i64  │
╞══════╪══════╡
│ 1    ┆ 1    │
│ 2    ┆ 1    │
│ 3    ┆ 3    │
└──────┴──────┘
```

You can find other fill strategies in the API docs.

### Fill with an expression

For more flexibility we can fill the missing data with an expression. For example,
to fill nulls with the median value from that column:

=== ":fontawesome-brands-python: Python"
    ``` python
    --8<-- "user-guide/python/expressions/null.py:fillexpr"
    ```


```text
shape: (3, 2)
┌──────┬──────┐
│ col1 ┆ col2 │
│ ---  ┆ ---  │
│ i64  ┆ f64  │
╞══════╪══════╡
│ 1    ┆ 1.0  │
│ 2    ┆ 2.0  │
│ 3    ┆ 3.0  │
└──────┴──────┘
```

In this case the column is cast from integer to float because the median is a float statistic.

### Fill with interpolation

In addition, we can fill nulls with interpolation (without using the `fill_null` function):

=== ":fontawesome-brands-python: Python"
    ``` python
    --8<-- "user-guide/python/expressions/null.py:fillinterpolate"
    ```


```text
shape: (3, 2)
┌──────┬──────┐
│ col1 ┆ col2 │
│ ---  ┆ ---  │
│ i64  ┆ i64  │
╞══════╪══════╡
│ 1    ┆ 1    │
│ 2    ┆ 2    │
│ 3    ┆ 3    │
└──────┴──────┘
```


## `NotaNumber` or `NaN` values

Missing data in a `Series` has a `null` value. However, you can use `NotaNumber` or `NaN` values in columns with float datatypes. These `NaN` values can be created from Numpy's `np.nan` or the native python `float('nan')`:

=== ":fontawesome-brands-python: Python"
    ``` python
    --8<-- "user-guide/python/expressions/null.py:nan"
    ```


```text
shape: (4, 1)
┌───────┐
│ value │
│ ---   │
│ f64   │
╞═══════╡
│ 1.0   │
│ NaN   │
│ NaN   │
│ 3.0   │
└───────┘
```

!!! info
    In `Pandas` by default a `NaN` value in an integer column causes the column to be cast to float. This does not happen in `Polars` - instead an exception is raised.

`NaN` values are considered to be a type of floating point data and are **not considered to be missing data** in `Polars`. This means:

- `NaN` values are **not** counted with the `null_count` method
- `NaN` values are filled when you use `fill_nan` method but are **not** filled with the `fill_null` method

`Polars` has `is_nan` and `fill_nan` methods which work in a similar way to the `is_null` and `fill_null` methods. The underlying Arrow arrays do not have a pre-computed validity bitmask for `NaN` values so this has to be computed for the `is_nan` method.

One further difference between `null` and `NaN` values is that taking the `mean` of a column with `null` values excludes the `null` values from the calculation but with `NaN` values taking the mean results in a `NaN`. This behaviour can be avoided by replacing the `NaN` values with `null` values;

=== ":fontawesome-brands-python: Python"
    ``` python
    --8<-- "user-guide/python/expressions/null.py:nanfill"
    ```

```text
shape: (1, 1)
┌───────┐
│ value │
│ ---   │
│ f64   │
╞═══════╡
│ 2.0   │
└───────┘
```