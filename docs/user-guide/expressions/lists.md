# Lists

An expression context we haven't discussed yet is the `List` context. This means simply we can apply any expression on the elements of a `List`.

# Row wise computations

This context is ideal for computing things in row orientation.

Polars expressions work on columns that have the guarantee that they consist of homogeneous data.
Columns have this guarantee, rows in a `DataFrame` not so much.
Luckily we have a data type that has the guarantee that the rows are homogeneous: `pl.List` data type.

Let's say we have the following data:

{{code_block('user-guide/expressions/lists','dataframe',['DataFrame'])}}

```python exec="on" result="text" session="user-guide/lists"
--8<-- "python/user-guide/expressions/lists.py:setup"
--8<-- "python/user-guide/expressions/lists.py:dataframe"
```


If we want to compute the `rank` of all the columns except for `"student"`, we can collect those into a `list` data type:

This would give:

{{code_block('user-guide/expressions/lists','rank',['concat_list'])}}

```python exec="on" result="text" session="user-guide/lists"
--8<-- "python/user-guide/expressions/lists.py:rank"
```

## Running polars expression on list elements

We can run **any** polars expression on the elements of a list with the `arr.eval` (`arr().eval` in Rust) expression! These expressions run entirely on polars' query engine and can run in parallel so will be super fast.

Let's expand the example from above with something a little more interesting. Pandas allows you to compute the percentages of the `rank` values. Polars doesn't provide such a keyword argument. But because expressions are so versatile we can create our own percentage rank expression. Let's try that!

Note that we must `select` the list's element from the context. When we apply expressions over list elements, we use `pl.element()` to select the element of a list.

{{code_block('user-guide/expressions/lists','expression',['arr.eval'])}}

```python exec="on" result="text" session="user-guide/lists"
--8<-- "python/user-guide/expressions/lists.py:expression"
```

Note that this solution works for any expressions/operation you want to do row wise.