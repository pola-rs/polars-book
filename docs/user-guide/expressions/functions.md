# Functions

`Polars` expressions have a large number of built in functions. These allow you to create complex queries without the need for [user defined functions](user-defined-functions.md). There are too many to go through here, but we will cover some of the more popular use cases. If you want to view all the functions go to the API Reference for your programming language.

In the examples below we will use the following `DataFrame`:

{{code_block('user-guide/expressions/functions','dataframe',['DataFrame'])}}

```python exec="on" result="text" session="user-guide/functions"
--8<-- "python/user-guide/expressions/functions.py:setup"
--8<-- "python/user-guide/expressions/functions.py:dataframe"
```

## Column Selection

There are various convenience methods to select multiple or all columns. 

### Select All Columns

{{code_block('user-guide/expressions/functions','all',['all'])}}


### Select All Columns Except

{{code_block('user-guide/expressions/functions','exclude',['exclude'])}}

```python exec="on" result="text" session="user-guide/functions"
--8<-- "python/user-guide/expressions/functions.py:exclude"
```

## Functional Selectors

Polars also allows for the use of intuitive selections for columns based on their name, `dtype` or other properties; and this is built on top of existing functionality outlined in `col` used above. It is recommended to use them by importing and aliasing `polars.selectors` as `cs`. For example, in this dataset:

{{code_block('user-guide/expressions/functions','selectors_df',['DataFrame'])}}

```python exec="on" result="text" session="user-guide/functions"
--8<-- "python/user-guide/expressions/functions.py:selectors_df"
```

### Matching by `dtype`

To select just the integer and string columns, we can do:

{{code_block('user-guide/expressions/functions','selectors_intro',['selectors'])}}

```python exec="on" result="text" session="user-guide/functions"
--8<-- "python/user-guide/expressions/functions.py:selectors_intro"
```

### Applying set operations

These *selectors* also allow for set based selection operations. For instance, to select the **numeric** columns **except** the **first** column that indicates row numbers:

{{code_block('user-guide/expressions/functions','selectors_diff',['cs_first', 'cs_numeric'])}}

```python exec="on" result="text" session="user-guide/functions"
--8<-- "python/user-guide/expressions/functions.py:selectors_diff"
```

We can also select the row number by name **and** any **non**-numeric columns:

{{code_block('user-guide/expressions/functions','selectors_union',['cs_by_name', 'cs_numeric'])}}

```python exec="on" result="text" session="user-guide/functions"
--8<-- "python/user-guide/expressions/functions.py:selectors_union"
```

### Pattern and substring matching

*Selectors* can also be matched by substring and regex pattern:

{{code_block('user-guide/expressions/functions','selectors_by_name',['cs_contains', 'cs_matches'])}}

```python exec="on" result="text" session="user-guide/functions"
--8<-- "python/user-guide/expressions/functions.py:selectors_by_name"
```

### Converting to expressions

What if we want to apply a specific operation on the selected columns (i.e. get back to representing them as **expressions** to operate upon)? We can simply convert them using `as_expr` and then proceed as normal:

{{code_block('user-guide/expressions/functions','selectors_to_expr',['cs.temporal'])}}

```python exec="on" result="text" session="user-guide/functions"
--8<-- "python/user-guide/expressions/functions.py:selectors_to_expr"
```

## Column Naming

By default if you perform a expression it will keep the same name as the original column. In the example below we perform an expression on the `nrs` column. Note that the output `DataFrame` still has the same name.

{{code_block('user-guide/expressions/functions','samename',[])}}

=== ":fontawesome-brands-python: Python"
    ``` python
    --8<-- "python/user-guide/expressions/functions.py:samename"
    ```

```python exec="on" result="text" session="user-guide/functions"
--8<-- "python/user-guide/expressions/functions.py:samename"
```

This might get problematic in the case you use the same column multiple times in your expression as the output columns will get duplicated. For example the following query will fail.

{{code_block('user-guide/expressions/functions','samenametwice',[])}}

```python exec="on" result="text" session="user-guide/functions"
--8<-- "python/user-guide/expressions/functions.py:samenametwice"
```

You can change the output name of an expression by using the `alias` function 

{{code_block('user-guide/expressions/functions','samenamealias',['alias'])}}

```python exec="on" result="text" session="user-guide/functions"
--8<-- "python/user-guide/expressions/functions.py:samenamealias"
```

In case of multiple columns for example when using `all()` or `col(*)` you can apply a mapping function `map_alias`  to change the original column name into something else. In case you want to add a suffix (`suffix()`) or prefix (`prefix()`) these are also built in. 

=== ":fontawesome-brands-python: Python"
    [:material-api:  `prefix`](https://pola-rs.github.io/polars/py-polars/html/reference/expressions/api/polars.Expr.prefix.html)
    [:material-api:  `suffix`](https://pola-rs.github.io/polars/py-polars/html/reference/expressions/api/polars.Expr.suffix.html)
    [:material-api:  `map_alias`](https://pola-rs.github.io/polars/py-polars/html/reference/expressions/api/polars.Expr.map_alias.html)

## Count Unique Values

There are two ways to count unique values in `Polars`: an exact methodology, and an approximation. The approximation uses the [HyperLogLog++](https://en.wikipedia.org/wiki/HyperLogLog) algorithm to approximate the cardinality and is especially useful for very large datasets where an approximation is good enough.


{{code_block('user-guide/expressions/functions','countunique',['n_unique','approx_unique'])}}

```python exec="on" result="text" session="user-guide/functions"
--8<-- "python/user-guide/expressions/functions.py:countunique"
```

## Conditionals

`Polars` supports if-else like conditions in expressions with the `when`, `then`, `otherwise` syntax. The predicate is placed in the `when` clause and when this evaluates to `true` the `then` expression is applied otherwise the `otherwise` expression is applied (row-wise).

{{code_block('user-guide/expressions/functions','conditional',['when'])}}

```python exec="on" result="text" session="user-guide/functions"
--8<-- "python/user-guide/expressions/functions.py:conditional"
```
