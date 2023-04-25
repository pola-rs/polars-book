# Lists

An expression context we haven't discussed yet is the `List` context. This means simply we can apply any expression on the elements of a `List`.

# Row wise computations

This context is ideal for computing things in row orientation.

Polars expressions work on columns that have the guarantee that they consist of homogeneous data.
Columns have this guarantee, rows in a `DataFrame` not so much.
Luckily we have a data type that has the guarantee that the rows are homogeneous: `pl.List` data type.

Let's say we have the following data:

=== ":fontawesome-brands-python: Python"
    [:material-api:  `DataFrame`](https://pola-rs.github.io/polars/py-polars/html/reference/dataframe/index.html#dataframe)
    ``` python
    --8<-- "user-guide/python/expressions/lists.py:dataframe"
    ```

```python exec="on" result="text" session="user-guide/lists"
--8<-- "user-guide/python/expressions/lists.py:setup"
--8<-- "user-guide/python/expressions/lists.py:dataframe"
```


If we want to compute the `rank` of all the columns except for `"student"`, we can collect those into a `list` data type:

This would give:

=== ":fontawesome-brands-python: Python"
    [:material-api:  `concat_list`](https://pola-rs.github.io/polars/py-polars/html/reference/expressions/api/polars.concat_list.html)
    ``` python
    --8<-- "user-guide/python/expressions/lists.py:rank"
    ```

```python exec="on" result="text" session="user-guide/lists"
--8<-- "user-guide/python/expressions/lists.py:rank"
```

## Running polars expression on list elements

We can run **any** polars expression on the elements of a list with the `arr.eval` (`arr().eval` in Rust) expression! These expressions run entirely on polars' query engine and can run in parallel so will be super fast.

Let's expand the example from above with something a little more interesting. Pandas allows you to compute the percentages of the `rank` values. Polars doesn't provide such a keyword argument. But because expressions are so versatile we can create our own percentage rank expression. Let's try that!

Note that we must `select` the list's element from the context. When we apply expressions over list elements, we use `pl.element()` to select the element of a list.

=== ":fontawesome-brands-python: Python"
    [:material-api:  `arr.eval`](https://pola-rs.github.io/polars/py-polars/html/reference/expressions/api/polars.Expr.arr.eval.html)
    ``` python
    --8<-- "user-guide/python/expressions/lists.py:expression"
    ```

```python exec="on" result="text" session="user-guide/lists"
--8<-- "user-guide/python/expressions/lists.py:expression"
```

Note that this solution works for any expressions/operation you want to do row wise.