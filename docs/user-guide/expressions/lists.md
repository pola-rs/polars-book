# Lists and Arrays

`Polars` has first-class support for `List` columns: that is, columns where each row is a list of homogenous elements, of varying lengths. `Polars` also has an `Array` datatype, which is analogus to `numpy`'s `ndarray` objects, where the length is identical across rows.

Note: this is different from Python's `List` object, where the elements can be of any time. Polars can store these within columns, but as a generic `Object` datatype that doesn't have the special list manipulation features that we're about to discuss.

# Powerful *List* manipulation

Let's say we had the following data from different weather stations across a state. When the weather station is unable to get a result, an error code is recorded instead of the actual temperature at that time.

{{code_block('user-guide/expressions/lists','weather_df',['DataFrame'])}}
```python exec="on" result="text" session="user-guide/lists"
--8<-- "python/user-guide/expressions/lists.py:setup"
--8<-- "python/user-guide/expressions/lists.py:weather_df"
```

## Creating a *List* column

For the `weather` `DataFrame` created above, it's very likely we need to run some analysis on the temperatures that are captured by each station. To make this happen, we need to first be able to get individual temperature measurements. This is done by:

{{code_block('user-guide/expressions/lists','string_to_list',['str.split'])}}
```python exec="on" result="text" session="user-guide/lists"
--8<-- "python/user-guide/expressions/lists.py:string_to_list"
```

One way we could go post this would be to convert each temperature measurement into its own row:

{{code_block('user-guide/expressions/lists','explode_to_atomic',['list.explode'])}}
```python exec="on" result="text" session="user-guide/lists"
--8<-- "python/user-guide/expressions/lists.py:explode_to_atomic"
```

However, in Polars, we often do not need to do this!

## Operating on *List* columns

Polars provides several standard operations on `List` columns. If we want the first three measurements, we can do a `head(3)`. The last three can be obtained via a `tail(3)`, or alternately, via `slice` (negative indexing is supported). We can also identify the number of observations via `lengths`. Let's see them in action:

{{code_block('user-guide/expressions/lists','list_ops',['list_ops'])}}
```python exec="on" result="text" session="user-guide/lists"
--8<-- "python/user-guide/expressions/lists.py:list_ops"
```

## Element-wise computation within *List*s

If we need to identify the stations that are giving the most number of errors from the starting `DataFrame`, we need to:

1. Parse the string input as a `List` of string values (already done).
2. Identify those strings that can be converted to numbers.
3. Identify the number of non-numeric values (i.e. `null` values) in the list, by row.
4. Rename this output as `errors` so that we can easily identify the stations.

The third step requires a casting (or alternately, a regex pattern search) operation to be perform on each element of the list. We can do this using by applying the operation on each element by first referencing them in the `pl.element()` context, and then calling a suitable Polars expression on them. Let's see how:

{{code_block('user-guide/expressions/lists','count_errors',['count_errors'])}}
```python exec="on" result="text" session="user-guide/lists"
--8<-- "python/user-guide/expressions/lists.py:count_errors"
```

What if we chose the regex route (i.e. recognizing the presence of *any* alphabetical character?)

{{code_block('user-guide/expressions/lists','count_errors_regex',['count_errors_regex'])}}
```python exec="on" result="text" session="user-guide/lists"
--8<-- "python/user-guide/expressions/lists.py:count_errors_regex"
```

If you're unfamiliar with the `(?i)`, it's a good time to look at the [`str.contains`](https://pola-rs.github.io/polars/py-polars/html/reference/expressions/api/polars.Expr.str.contains.html#polars-expr-str-contains) documentation for Polars! The rust regex crate provides a lot of additional regex flags that might come in handy.

# Row-wise computations

This context is ideal for computing things in row orientation.

Polars expressions work on columns that have the guarantee that they consist of homogeneous data. Columns have this guarantee, rows in a `DataFrame` not so much. Luckily we have a data type that has the guarantee that the rows are homogeneous: `pl.List` data type.  We can **any** Polars operations on the elements of the list with the `arr.eval` (`arr().eval` in Rust) expression! These expressions run entirely on polars' query engine and can run in parallel so will be super fast.

Let's say we have another set of weather data across three days, for different stations:

{{code_block('user-guide/expressions/lists','weather_by_day',['weather_by_day'])}}
```python exec="on" result="text" session="user-guide/lists"
--8<-- "python/user-guide/expressions/lists.py:weather_by_day"
```

Let's do something interesting. `pandas` allows you to compute the percentages of the rank values. `Polars` doesn't provide such a keyword argument. But because expressions are so versatile we can create our own percentage rank expression for highest temperature. Let's try that!

{{code_block('user-guide/expressions/lists','weather_by_day_rank',['weather_by_day_rank'])}}
```python exec="on" result="text" session="user-guide/lists"
--8<-- "python/user-guide/expressions/lists.py:weather_by_day_rank"
```

# Polars Arrays

`Array`s are a new data type that was recently introduced, and are still pretty nascent in features that it offers. The major difference between a `List` and an `Array` is that the latter is limited to having the same number of elements per row, while a `List` can have a variable number of elements. Both still require that each element's data type is the same.

We can define `Array` columns in this manner:

{{code_block('user-guide/expressions/lists','array_df',['array_df'])}}
```python exec="on" result="text" session="user-guide/lists"
--8<-- "python/user-guide/expressions/lists.py:array_df"
```

Basic operations are available on it (see Array for details).
