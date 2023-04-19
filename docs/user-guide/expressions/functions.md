# Functions

`Polars` expressions have a large number of build in functions. These allow you to create complex queries without the need for [user defined functions](user-defined-functions.md). There are too many to go through here, but we will cover some of the more popular use cases. If you want to view all the functions go to the API Reference for your programming language.

In the examples below we will use the following `DataFrame`:

=== ":fontawesome-brands-python: Python"
    ``` python
    --8<-- "user-guide/python/expressions/functions.py:dataframe"
    ```

```
shape: (5, 4)
┌──────┬───────┬──────────┬────────┐
│ nrs  ┆ names ┆ random   ┆ groups │
│ ---  ┆ ---   ┆ ---      ┆ ---    │
│ i64  ┆ str   ┆ f64      ┆ str    │
╞══════╪═══════╪══════════╪════════╡
│ 1    ┆ foo   ┆ 0.154163 ┆ A      │
│ 2    ┆ ham   ┆ 0.74005  ┆ A      │
│ 3    ┆ spam  ┆ 0.263315 ┆ B      │
│ null ┆ egg   ┆ 0.533739 ┆ C      │
│ 5    ┆ null  ┆ 0.014575 ┆ B      │
└──────┴───────┴──────────┴────────┘
```

#### Column Selection

There are various convenience methods to select multiple or all columns. 

##### Select All Columns

=== ":fontawesome-brands-python: Python"
    ``` python
    --8<-- "user-guide/python/expressions/functions.py:all"
    ```

##### Select All Columns Except

=== ":fontawesome-brands-python: Python"
    ``` python
    --8<-- "user-guide/python/expressions/functions.py:exclude"
    ```

```
shape: (5, 3)
┌──────┬───────┬──────────┐
│ nrs  ┆ names ┆ random   │
│ ---  ┆ ---   ┆ ---      │
│ i64  ┆ str   ┆ f64      │
╞══════╪═══════╪══════════╡
│ 1    ┆ foo   ┆ 0.154163 │
│ 2    ┆ ham   ┆ 0.74005  │
│ 3    ┆ spam  ┆ 0.263315 │
│ null ┆ egg   ┆ 0.533739 │
│ 5    ┆ spam  ┆ 0.014575 │
└──────┴───────┴──────────┘
```

#### Column Naming

By default if you perform a expression it will keep the same name as the original column. In the example below we perform an expression on the `nrs` column. Note that the output `DataFrame` still has the same name.

=== ":fontawesome-brands-python: Python"
    ``` python
    --8<-- "user-guide/python/expressions/functions.py:samename"
    ```

```
shape: (5, 1)
┌──────┐
│ nrs  │
│ ---  │
│ i64  │
╞══════╡
│ 6    │
│ 7    │
│ 8    │
│ null │
│ 10   │
└──────┘
```

This might get problematic in case you use the same column muliple times in your expression as the output columns will get duplicated. For example the following query will fail.

=== ":fontawesome-brands-python: Python"
    ``` python
    --8<-- "user-guide/python/expressions/functions.py:samenametwice"
    ```

```
column with name 'nrs' has more than one occurrences
```

You can change the output name of an expression by using the `alias` function 

=== ":fontawesome-brands-python: Python"
    ``` python
    --8<-- "user-guide/python/expressions/functions.py:samenamealias"
    ```

```
shape: (5, 2)
┌─────────┬─────────┐
│ nrs + 5 ┆ nrs - 5 │
│ ---     ┆ ---     │
│ i64     ┆ i64     │
╞═════════╪═════════╡
│ 6       ┆ -4      │
│ 7       ┆ -3      │
│ 8       ┆ -2      │
│ null    ┆ null    │
│ 10      ┆ 0       │
└─────────┴─────────┘
```

In case of multiple columns for example when using `all()` or `col(*)` you can apply a mapping function `map_alias`  to change the original column name into something else. In case you want to add a suffix (`suffix()`) or prefix (`prefix()`) these are also build in. 

=== ":fontawesome-brands-python: Python"
    [:material-api:  `prefix`](https://pola-rs.github.io/polars/py-polars/html/reference/expressions/api/polars.Expr.prefix.html)
    [:material-api:  `suffix`](https://pola-rs.github.io/polars/py-polars/html/reference/expressions/api/polars.Expr.suffix.html)
    [:material-api:  `map_alias`](https://pola-rs.github.io/polars/py-polars/html/reference/expressions/api/polars.Expr.map_alias.html)

##### Count Unique Values

There are two ways two count unique values in `Polars` one is an exact methodology and the other one is an approximantion. The approximation uses the [HyperLogLog++](https://en.wikipedia.org/wiki/HyperLogLog) algorithm to approximate the cardinality and is especially usefull for very large datasets where an approximation is good enough.


=== ":fontawesome-brands-python: Python"
    ``` python
    --8<-- "user-guide/python/expressions/functions.py:countunique"
    ```

```
shape: (1, 2)
┌────────┬───────────────┐
│ unique ┆ unique_approx │
│ ---    ┆ ---           │
│ u32    ┆ u32           │
╞════════╪═══════════════╡
│ 4      ┆ 4             │
└────────┴───────────────┘
```

##### Null Support

TODO

##### Clipping

TODO

##### Conditionals

TODO
