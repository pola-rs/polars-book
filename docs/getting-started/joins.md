# Combining DataFrames

There are two ways `DataFrame`s can be combined depending on the use case: join and concat.

## Join

Polars supports all types of join (e.g. left, right, inner, outer). Let's have a closer look on how to `join` two `DataFrames` into a single `DataFrame`. Our two `DataFrames` both have an 'id'-like column: `a` and `x`. We can use those columns to `join` the `DataFrames` in this example.

=== ":fontawesome-brands-python: Python"

    ``` python
    --8<-- "getting-started/python/joins.py:join"
    ```

=== ":fontawesome-brands-rust: Rust"

    ``` rust
    --8<-- "getting-started/rust/joins.rs:join"
    ```
=== ":fontawesome-brands-node-js: NodeJS"

    ``` javaScript
    --8<-- "getting-started/node/joins.js:join"
    ```

```
shape: (8, 4)
┌─────┬──────────┬───────┬─────┐
│ a   ┆ b        ┆ d     ┆ y   │
│ --- ┆ ---      ┆ ---   ┆ --- │
│ f64 ┆ f64      ┆ f64   ┆ str │
╞═════╪══════════╪═══════╪═════╡
│ 0.0 ┆ 0.568449 ┆ 1.0   ┆ A   │
├╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌┼╌╌╌╌╌┤
│ 1.0 ┆ 0.252443 ┆ 2.0   ┆ A   │
├╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌┼╌╌╌╌╌┤
│ 2.0 ┆ 0.708543 ┆ null  ┆ A   │
├╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌┼╌╌╌╌╌┤
│ 3.0 ┆ 0.08118  ┆ null  ┆ B   │
├╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌┼╌╌╌╌╌┤
│ 4.0 ┆ 0.449587 ┆ 0.0   ┆ B   │
├╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌┼╌╌╌╌╌┤
│ 5.0 ┆ 0.443502 ┆ -5.0  ┆ C   │
├╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌┼╌╌╌╌╌┤
│ 6.0 ┆ 0.434625 ┆ -42.0 ┆ X   │
├╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌┼╌╌╌╌╌┤
│ 7.0 ┆ 0.372544 ┆ null  ┆ X   │
└─────┴──────────┴───────┴─────┘

```

## Concat

We can also `concatenate` two `DataFrames`. Vertical concatenation will make the `DataFrame` longer. Horizontal concatenation will make the `DataFrame` wider. Below you can see the result of an horizontal concatenation of our two `DataFrames`.

=== ":fontawesome-brands-python: Python"

    ``` python
    --8<-- "getting-started/python/joins.py:hstack"
    ```

=== ":fontawesome-brands-rust: Rust"

    ``` rust
    --8<-- "getting-started/rust/joins.rs:hstack"
    ```
=== ":fontawesome-brands-node-js: NodeJS"

    ``` javaScript
    --8<-- "getting-started/node/joins.js:hstack"
    ```

```
shape: (8, 5)
┌─────┬──────────┬───────┬─────┬─────┐
│ a   ┆ b        ┆ d     ┆ x   ┆ y   │
│ --- ┆ ---      ┆ ---   ┆ --- ┆ --- │
│ f64 ┆ f64      ┆ f64   ┆ f64 ┆ str │
╞═════╪══════════╪═══════╪═════╪═════╡
│ 0.0 ┆ 0.568449 ┆ 1.0   ┆ 0.0 ┆ A   │
├╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌┼╌╌╌╌╌┼╌╌╌╌╌┤
│ 1.0 ┆ 0.252443 ┆ 2.0   ┆ 1.0 ┆ A   │
├╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌┼╌╌╌╌╌┼╌╌╌╌╌┤
│ 2.0 ┆ 0.708543 ┆ null  ┆ 2.0 ┆ A   │
├╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌┼╌╌╌╌╌┼╌╌╌╌╌┤
│ 3.0 ┆ 0.08118  ┆ null  ┆ 3.0 ┆ B   │
├╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌┼╌╌╌╌╌┼╌╌╌╌╌┤
│ 4.0 ┆ 0.449587 ┆ 0.0   ┆ 4.0 ┆ B   │
├╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌┼╌╌╌╌╌┼╌╌╌╌╌┤
│ 5.0 ┆ 0.443502 ┆ -5.0  ┆ 5.0 ┆ C   │
├╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌┼╌╌╌╌╌┼╌╌╌╌╌┤
│ 6.0 ┆ 0.434625 ┆ -42.0 ┆ 6.0 ┆ X   │
├╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌┼╌╌╌╌╌┼╌╌╌╌╌┤
│ 7.0 ┆ 0.372544 ┆ null  ┆ 7.0 ┆ X   │
└─────┴──────────┴───────┴─────┴─────┘

```