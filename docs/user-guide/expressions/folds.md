# Folds

`Polars` provides expressions/methods for horizontal aggregations like `sum`,`min`, `mean`,
etc. by setting the argument `axis=1`. However, when you need a more complex aggregation the default methods `Polars` may not be sufficient. That's when `folds` come in handy.

The `fold` expression operates on columns for maximum speed. It utilizes the data layout very efficiently and often has vectorized execution.

### Manual Sum

Let's start with an example by implementing the `sum` operation ourselves, with a `fold`.

=== ":fontawesome-brands-python: Python"
    ``` python
    --8<-- "user-guide/python/expressions/folds.py:mansum"
    ```

```
shape: (3, 1)
┌─────┐
│ sum │
│ --- │
│ i64 │
╞═════╡
│ 11  │
│ 22  │
│ 33  │
└─────┘
```


The snippet above recursively applies the function `f(acc, x) -> acc` to an accumulator `acc` and a new column `x`. The function operates on columns individually and can take advantage of cache efficiency and vectorization.

### Conditional

In the case where you'd want to apply a condition/predicate on all columns in a `DataFrame` a `fold` operation can be a very concise way to express this.

=== ":fontawesome-brands-python: Python"
    ``` python
    --8<-- "user-guide/python/expressions/folds.py:conditional"
    ```

```
shape: (1, 2)
┌─────┬─────┐
│ a   ┆ b   │
│ --- ┆ --- │
│ i64 ┆ i64 │
╞═════╪═════╡
│ 3   ┆ 2   │
└─────┴─────┘
```

In the snippet we filter all rows where **each** column value is `> 1`.

### Folds and string data

Folds could be used to concatenate string data. However, due to the materialization of intermediate columns, this operation will have squared complexity.

Therefore, we recommend using the `concat_str` expression for this.

=== ":fontawesome-brands-python: Python"
    ``` python
    --8<-- "user-guide/python/expressions/folds.py:string"
    ```

```
shape: (3, 1)
┌─────┐
│ a   │
│ --- │
│ str │
╞═════╡
│ a1  │
│ b2  │
│ c3  │
└─────┘
```