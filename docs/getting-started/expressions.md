## Expressions

`Expressions` are the core strength of `Polars`. The `expressions` offer a versatile structure that solves easy queries, but is easily extended to complex analyses. Below we will cover the basic components that serve as building block for all your queries.

- `select`
- `filter`
- `with_columns`

### Select statement

To select a column we need to do two things. Define the `DataFrame` we want the data from. And second, select the data that we need. In the example below you see that we select `col('*')`. The asterisk stands for all columns.

=== ":fontawesome-brands-python: Python"
    [:material-api:  `select`](https://pola-rs.github.io/polars/py-polars/html/reference/dataframe/api/polars.DataFrame.select.html)
    ``` python
    --8<-- "getting-started/python/expressions.py:select"
    ```

=== ":fontawesome-brands-rust: Rust"
    [:material-api:  `select`](https://pola-rs.github.io/polars/polars_core/frame/struct.DataFrame.html#method.select)
    ``` rust
    --8<-- "getting-started/rust/expressions.rs:select"
    ```
=== ":fontawesome-brands-node-js: NodeJS"
    [:material-api:  `select`](https://pola-rs.github.io/nodejs-polars/interfaces/DataFrame-1.html#select)
    ``` javaScript
    --8<-- "getting-started/node/expressions.js:select"
    ```

```
shape: (8, 4)
┌─────┬──────────┬─────────────────────┬───────┐
│ a   ┆ b        ┆ c                   ┆ d     │
│ --- ┆ ---      ┆ ---                 ┆ ---   │
│ i64 ┆ f64      ┆ datetime[μs]        ┆ f64   │
╞═════╪══════════╪═════════════════════╪═══════╡
│ 0   ┆ 0.164545 ┆ 2022-12-01 00:00:00 ┆ 1.0   │
├╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌┤
│ 1   ┆ 0.747291 ┆ 2022-12-02 00:00:00 ┆ 2.0   │
├╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌┤
│ 2   ┆ 0.889227 ┆ 2022-12-03 00:00:00 ┆ NaN   │
├╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌┤
│ 3   ┆ 0.736651 ┆ 2022-12-04 00:00:00 ┆ NaN   │
├╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌┤
│ 4   ┆ 0.099687 ┆ 2022-12-05 00:00:00 ┆ 0.0   │
├╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌┤
│ 5   ┆ 0.965809 ┆ 2022-12-06 00:00:00 ┆ -5.0  │
├╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌┤
│ 6   ┆ 0.93697  ┆ 2022-12-07 00:00:00 ┆ -42.0 │
├╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌┤
│ 7   ┆ 0.848925 ┆ 2022-12-08 00:00:00 ┆ null  │
└─────┴──────────┴─────────────────────┴───────┘
```

You can also specify the specific columns that you want to return. There are two ways to do this. The first option is to create a `list` of column names, as seen below.

=== ":fontawesome-brands-python: Python"
    [:material-api:  `select`](https://pola-rs.github.io/polars/py-polars/html/reference/dataframe/api/polars.DataFrame.select.html)
    ``` python
    --8<-- "getting-started/python/expressions.py:select2"
    ```

=== ":fontawesome-brands-rust: Rust"
    [:material-api:  `select`](https://pola-rs.github.io/polars/polars_core/frame/struct.DataFrame.html#method.select)
    ``` rust
    --8<-- "getting-started/rust/expressions.rs:select2"
    ```
=== ":fontawesome-brands-node-js: NodeJS"
    [:material-api:  `select`](https://pola-rs.github.io/nodejs-polars/interfaces/DataFrame-1.html#select)
    ``` javaScript
    --8<-- "getting-started/node/expressions.js:select2"
    ```

```
shape: (8, 2)
┌─────┬──────────┐
│ a   ┆ b        │
│ --- ┆ ---      │
│ i64 ┆ f64      │
╞═════╪══════════╡
│ 0   ┆ 0.164545 │
├╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┤
│ 1   ┆ 0.747291 │
├╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┤
│ 2   ┆ 0.889227 │
├╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┤
│ 3   ┆ 0.736651 │
├╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┤
│ 4   ┆ 0.099687 │
├╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┤
│ 5   ┆ 0.965809 │
├╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┤
│ 6   ┆ 0.93697  │
├╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┤
│ 7   ┆ 0.848925 │
└─────┴──────────┘
```

The second option is to specify each column within a `list` in the `select` statement. This option is shown below.

=== ":fontawesome-brands-python: Python"
    [:material-api:  `select`](https://pola-rs.github.io/polars/py-polars/html/reference/dataframe/api/polars.DataFrame.select.html)
    ``` python
    --8<-- "getting-started/python/expressions.py:select3"
    ```

=== ":fontawesome-brands-rust: Rust"
    [:material-api:  `select`](https://pola-rs.github.io/polars/polars_core/frame/struct.DataFrame.html#method.select)
    ``` rust
    --8<-- "getting-started/rust/expressions.rs:select3"
    ```
=== ":fontawesome-brands-node-js: NodeJS"
    [:material-api:  `select`](https://pola-rs.github.io/nodejs-polars/interfaces/DataFrame-1.html#select)
    ``` javaScript
    --8<-- "getting-started/node/expressions.js:select3"
    ```

```
shape: (3, 2)
┌─────┬──────────┐
│ a   ┆ b        │
│ --- ┆ ---      │
│ i64 ┆ f64      │
╞═════╪══════════╡
│ 0   ┆ 0.164545 │
├╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┤
│ 1   ┆ 0.747291 │
├╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┤
│ 2   ┆ 0.889227 │
└─────┴──────────┘
```

If you want to exclude an entire column from your view, you can simply use `exclude` in your `select` statement.

=== ":fontawesome-brands-python: Python"
    [:material-api:  `select`](https://pola-rs.github.io/polars/py-polars/html/reference/dataframe/api/polars.DataFrame.select.html)
    ``` python
    --8<-- "getting-started/python/expressions.py:exclude"
    ```

=== ":fontawesome-brands-rust: Rust"
    [:material-api:  `select`](https://pola-rs.github.io/polars/polars_core/frame/struct.DataFrame.html#method.select)
    ``` rust
    --8<-- "getting-started/rust/expressions.rs:exclude"
    ```
=== ":fontawesome-brands-node-js: NodeJS"
    [:material-api:  `select`](https://pola-rs.github.io/nodejs-polars/interfaces/DataFrame-1.html#select)
    ``` javaScript
    --8<-- "getting-started/node/expressions.js:exclude"
    ```

```
shape: (8, 3)
┌──────────┬─────────────────────┬───────┐
│ b        ┆ c                   ┆ d     │
│ ---      ┆ ---                 ┆ ---   │
│ f64      ┆ datetime[μs]        ┆ f64   │
╞══════════╪═════════════════════╪═══════╡
│ 0.220182 ┆ 2022-12-01 00:00:00 ┆ 1.0   │
├╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌┤
│ 0.750839 ┆ 2022-12-02 00:00:00 ┆ 2.0   │
├╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌┤
│ 0.634639 ┆ 2022-12-03 00:00:00 ┆ NaN   │
├╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌┤
│ 0.67404  ┆ 2022-12-04 00:00:00 ┆ NaN   │
├╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌┤
│ 0.102818 ┆ 2022-12-05 00:00:00 ┆ 0.0   │
├╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌┤
│ 0.896408 ┆ 2022-12-06 00:00:00 ┆ -5.0  │
├╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌┤
│ 0.062943 ┆ 2022-12-07 00:00:00 ┆ -42.0 │
├╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌┤
│ 0.108093 ┆ 2022-12-08 00:00:00 ┆ null  │
└──────────┴─────────────────────┴───────┘
```


### Filter

The `filter` option allows us to create a subset of the `DataFrame`. We use the same `DataFrame` as earlier and we filter between two specified dates.

=== ":fontawesome-brands-python: Python"
    [:material-api:  `filter`](https://pola-rs.github.io/polars/py-polars/html/reference/dataframe/api/polars.DataFrame.filter.html)
    ``` python
    --8<-- "getting-started/python/expressions.py:filter"
    ```

=== ":fontawesome-brands-rust: Rust"
    [:material-api:  `filter`](https://pola-rs.github.io/polars/polars_core/frame/struct.DataFrame.html#method.filter)
    ``` rust
    --8<-- "getting-started/rust/expressions.rs:filter"
    ```
=== ":fontawesome-brands-node-js: NodeJS"
    [:material-api:  `filter`](https://pola-rs.github.io/nodejs-polars/interfaces/DataFrame-1.html#filter)
    ``` javaScript
    --8<-- "getting-started/node/expressions.js:filter"
    ```

```
shape: (5, 4)
┌─────┬──────────┬─────────────────────┬───────┐
│ a   ┆ b        ┆ c                   ┆ d     │
│ --- ┆ ---      ┆ ---                 ┆ ---   │
│ i64 ┆ f64      ┆ datetime[μs]        ┆ f64   │
╞═════╪══════════╪═════════════════════╪═══════╡
│ 2   ┆ 0.634639 ┆ 2022-12-03 00:00:00 ┆ NaN   │
├╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌┤
│ 3   ┆ 0.67404  ┆ 2022-12-04 00:00:00 ┆ NaN   │
├╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌┤
│ 4   ┆ 0.102818 ┆ 2022-12-05 00:00:00 ┆ 0.0   │
├╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌┤
│ 5   ┆ 0.896408 ┆ 2022-12-06 00:00:00 ┆ -5.0  │
├╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌┤
│ 6   ┆ 0.062943 ┆ 2022-12-07 00:00:00 ┆ -42.0 │
└─────┴──────────┴─────────────────────┴───────┘
```

With `filter` you can also create more complex filters that include multiple columns.

=== ":fontawesome-brands-python: Python"
    [:material-api:  `filter`](https://pola-rs.github.io/polars/py-polars/html/reference/dataframe/api/polars.DataFrame.filter.html)
    ``` python
    --8<-- "getting-started/python/expressions.py:filter2"
    ```

=== ":fontawesome-brands-rust: Rust"
    [:material-api:  `filter`](https://pola-rs.github.io/polars/polars_core/frame/struct.DataFrame.html#method.filter)
    ``` rust
    --8<-- "getting-started/rust/expressions.rs:filter2"
    ```
=== ":fontawesome-brands-node-js: NodeJS"
    [:material-api:  `filter`](https://pola-rs.github.io/nodejs-polars/interfaces/DataFrame-1.html#filter)
    ``` javaScript
    --8<-- "getting-started/node/expressions.js:filter2"
    ```

```
shape: (2, 4)
┌─────┬──────────┬─────────────────────┬─────┐
│ a   ┆ b        ┆ c                   ┆ d   │
│ --- ┆ ---      ┆ ---                 ┆ --- │
│ i64 ┆ f64      ┆ datetime[μs]        ┆ f64 │
╞═════╪══════════╪═════════════════════╪═════╡
│ 0   ┆ 0.220182 ┆ 2022-12-01 00:00:00 ┆ 1.0 │
├╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌┤
│ 1   ┆ 0.750839 ┆ 2022-12-02 00:00:00 ┆ 2.0 │
└─────┴──────────┴─────────────────────┴─────┘
```

### With_columns

`with_columns` allows you to create new columns for you analyses. We create two new columns `e` and `b+42`. First we sum all values from column `b` and store the results in column `e`. After that we add `42` to the values of `b`. Creating a new column `b+42` to store these results.

=== ":fontawesome-brands-python: Python"
    [:material-api:  `with_columns`](https://pola-rs.github.io/polars/py-polars/html/reference/dataframe/api/polars.DataFrame.with_columns.html)
    ``` python
    --8<-- "getting-started/python/expressions.py:with_columns"
    ```

=== ":fontawesome-brands-rust: Rust"
    [:material-api:  `with_column`](https://pola-rs.github.io/polars/polars_core/frame/struct.DataFrame.html#method.with_column)
    ``` rust
    --8<-- "getting-started/rust/expressions.rs:with_columns"
    ```
=== ":fontawesome-brands-node-js: NodeJS"
    [:material-api:  `withColumns`](https://pola-rs.github.io/nodejs-polars/interfaces/DataFrame-1.html#withColumns)
    ``` javaScript
    --8<-- "getting-started/node/expressions.js:with_columns"
    ```

```
shape: (8, 6)
┌─────┬──────────┬─────────────────────┬───────┬──────────┬───────────┐
│ a   ┆ b        ┆ c                   ┆ d     ┆ e        ┆ b+42      │
│ --- ┆ ---      ┆ ---                 ┆ ---   ┆ ---      ┆ ---       │
│ i64 ┆ f64      ┆ datetime[μs]        ┆ f64   ┆ f64      ┆ f64       │
╞═════╪══════════╪═════════════════════╪═══════╪══════════╪═══════════╡
│ 0   ┆ 0.606396 ┆ 2022-12-01 00:00:00 ┆ 1.0   ┆ 4.126554 ┆ 42.606396 │
├╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌┤
│ 1   ┆ 0.404966 ┆ 2022-12-02 00:00:00 ┆ 2.0   ┆ 4.126554 ┆ 42.404966 │
├╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌┤
│ 2   ┆ 0.619193 ┆ 2022-12-03 00:00:00 ┆ NaN   ┆ 4.126554 ┆ 42.619193 │
├╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌┤
│ 3   ┆ 0.41586  ┆ 2022-12-04 00:00:00 ┆ NaN   ┆ 4.126554 ┆ 42.41586  │
├╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌┤
│ 4   ┆ 0.35721  ┆ 2022-12-05 00:00:00 ┆ 0.0   ┆ 4.126554 ┆ 42.35721  │
├╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌┤
│ 5   ┆ 0.726861 ┆ 2022-12-06 00:00:00 ┆ -5.0  ┆ 4.126554 ┆ 42.726861 │
├╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌┤
│ 6   ┆ 0.201782 ┆ 2022-12-07 00:00:00 ┆ -42.0 ┆ 4.126554 ┆ 42.201782 │
├╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌┤
│ 7   ┆ 0.794286 ┆ 2022-12-08 00:00:00 ┆ null  ┆ 4.126554 ┆ 42.794286 │
└─────┴──────────┴─────────────────────┴───────┴──────────┴───────────┘
```

### Groupby

We will create a new `DataFrame` for the Groupby functionality. This new `DataFrame` will include several 'groups' that we want to groupby.

=== ":fontawesome-brands-python: Python"
    [:material-api:  `DataFrame`](https://pola-rs.github.io/polars/py-polars/html/reference/dataframe/index.html)
    ``` python
    --8<-- "getting-started/python/expressions.py:dataframe2"
    ```

=== ":fontawesome-brands-rust: Rust"
    [:material-api:  `DataFrame`](https://pola-rs.github.io/polars/polars_core/frame/struct.DataFrame.html)
    ``` rust
    --8<-- "getting-started/rust/expressions.rs:dataframe2"
    ```
=== ":fontawesome-brands-node-js: NodeJS"
    [:material-api:  `DataFrame`](https://pola-rs.github.io/nodejs-polars/interfaces/DataFrame-1.html)
    ``` javaScript
    --8<-- "getting-started/node/expressions.js:dataframe2"
    ```

```
shape: (8, 2)
┌─────┬─────┐
│ x   ┆ y   │
│ --- ┆ --- │
│ i64 ┆ str │
╞═════╪═════╡
│ 0   ┆ A   │
├╌╌╌╌╌┼╌╌╌╌╌┤
│ 1   ┆ A   │
├╌╌╌╌╌┼╌╌╌╌╌┤
│ 2   ┆ A   │
├╌╌╌╌╌┼╌╌╌╌╌┤
│ 3   ┆ B   │
├╌╌╌╌╌┼╌╌╌╌╌┤
│ 4   ┆ B   │
├╌╌╌╌╌┼╌╌╌╌╌┤
│ 5   ┆ C   │
├╌╌╌╌╌┼╌╌╌╌╌┤
│ 6   ┆ X   │
├╌╌╌╌╌┼╌╌╌╌╌┤
│ 7   ┆ X   │
└─────┴─────┘
```

=== ":fontawesome-brands-python: Python"
    [:material-api:  `groupby`](https://pola-rs.github.io/polars/py-polars/html/reference/dataframe/api/polars.DataFrame.groupby.html)
    ``` python
    --8<-- "getting-started/python/expressions.py:groupby"
    ```

=== ":fontawesome-brands-rust: Rust"
    [:material-api:  `groupby`](https://pola-rs.github.io/polars/polars_core/frame/struct.DataFrame.html#method.groupby)
    ``` rust
    --8<-- "getting-started/rust/expressions.rs:groupby"
    ```
=== ":fontawesome-brands-node-js: NodeJS"
    [:material-api:  `groupBy`](https://pola-rs.github.io/nodejs-polars/interfaces/DataFrame-1.html#groupBy)
    ``` javaScript
    --8<-- "getting-started/node/expressions.js:groupby"
    ```

```
shape: (4, 2)
┌─────┬───────┐
│ y   ┆ count │
│ --- ┆ ---   │
│ str ┆ u32   │
╞═════╪═══════╡
│ A   ┆ 3     │
├╌╌╌╌╌┼╌╌╌╌╌╌╌┤
│ B   ┆ 2     │
├╌╌╌╌╌┼╌╌╌╌╌╌╌┤
│ C   ┆ 1     │
├╌╌╌╌╌┼╌╌╌╌╌╌╌┤
│ X   ┆ 2     │
└─────┴───────┘
```

=== ":fontawesome-brands-python: Python"
    [:material-api:  `groupby`](https://pola-rs.github.io/polars/py-polars/html/reference/dataframe/api/polars.DataFrame.groupby.html)
    ``` python
    --8<-- "getting-started/python/expressions.py:groupby2"
    ```

=== ":fontawesome-brands-rust: Rust"
    [:material-api:  `groupby`](https://pola-rs.github.io/polars/polars_core/frame/struct.DataFrame.html#method.groupby)
    ``` rust
    --8<-- "getting-started/rust/expressions.rs:groupby2"
    ```
=== ":fontawesome-brands-node-js: NodeJS"
    [:material-api:  `groupBy`](https://pola-rs.github.io/nodejs-polars/interfaces/DataFrame-1.html#groupBy)
    ``` javaScript
    --8<-- "getting-started/node/expressions.js:groupby2"
    ```

```
shape: (4, 3)
┌─────┬───────┬─────┐
│ y   ┆ count ┆ sum │
│ --- ┆ ---   ┆ --- │
│ str ┆ u32   ┆ i64 │
╞═════╪═══════╪═════╡
│ A   ┆ 3     ┆ 3   │
├╌╌╌╌╌┼╌╌╌╌╌╌╌┼╌╌╌╌╌┤
│ B   ┆ 2     ┆ 7   │
├╌╌╌╌╌┼╌╌╌╌╌╌╌┼╌╌╌╌╌┤
│ C   ┆ 1     ┆ 5   │
├╌╌╌╌╌┼╌╌╌╌╌╌╌┼╌╌╌╌╌┤
│ X   ┆ 2     ┆ 13  │
└─────┴───────┴─────┘
```

### Combining operations

Below are some examples on how to combine operations to create the `DataFrame` you require.


=== ":fontawesome-brands-python: Python"
    [:material-api:  `select`](https://pola-rs.github.io/polars/py-polars/html/reference/dataframe/api/polars.DataFrame.select.html) ·
    [:material-api:  `with_columns`](https://pola-rs.github.io/polars/py-polars/html/reference/dataframe/api/polars.DataFrame.with_columns.html)
    ``` python
    --8<-- "getting-started/python/expressions.py:combine"
    ```

=== ":fontawesome-brands-rust: Rust"
    [:material-api:  `select`](https://pola-rs.github.io/polars/polars_core/frame/struct.DataFrame.html#method.select) ·
    [:material-api:  `with_column`](https://pola-rs.github.io/polars/polars_core/frame/struct.DataFrame.html#method.with_column)
    ``` rust
    --8<-- "getting-started/rust/expressions.rs:combine"
    ```
=== ":fontawesome-brands-node-js: NodeJS"
    [:material-api:  `select`](https://pola-rs.github.io/nodejs-polars/interfaces/DataFrame-1.html#select) ·
    [:material-api:  `withColumns`](https://pola-rs.github.io/nodejs-polars/interfaces/DataFrame-1.html#withColumns)
    ``` javaScript
    --8<-- "getting-started/node/expressions.js:combine"
    ```

```
shape: (8, 3)
┌─────┬──────────┬──────────┐
│ a   ┆ b        ┆ a * b    │
│ --- ┆ ---      ┆ ---      │
│ i64 ┆ f64      ┆ f64      │
╞═════╪══════════╪══════════╡
│ 0   ┆ 0.220182 ┆ 0.0      │
├╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┤
│ 1   ┆ 0.750839 ┆ 0.750839 │
├╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┤
│ 2   ┆ 0.634639 ┆ 1.269277 │
├╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┤
│ 3   ┆ 0.67404  ┆ 2.022121 │
├╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┤
│ 4   ┆ 0.102818 ┆ 0.41127  │
├╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┤
│ 5   ┆ 0.896408 ┆ 4.482038 │
├╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┤
│ 6   ┆ 0.062943 ┆ 0.377657 │
├╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┤
│ 7   ┆ 0.108093 ┆ 0.756653 │
└─────┴──────────┴──────────┘
```

=== ":fontawesome-brands-python: Python"
    [:material-api:  `select`](https://pola-rs.github.io/polars/py-polars/html/reference/dataframe/api/polars.DataFrame.select.html) ·
    [:material-api:  `with_columns`](https://pola-rs.github.io/polars/py-polars/html/reference/dataframe/api/polars.DataFrame.with_columns.html)
    ``` python
    --8<-- "getting-started/python/expressions.py:combine2"
    ```

=== ":fontawesome-brands-rust: Rust"
    [:material-api:  `select`](https://pola-rs.github.io/polars/polars_core/frame/struct.DataFrame.html#method.select) ·
    [:material-api:  `with_column`](https://pola-rs.github.io/polars/polars_core/frame/struct.DataFrame.html#method.with_column)
    ``` rust
    --8<-- "getting-started/rust/expressions.rs:combine2"
    ```
=== ":fontawesome-brands-node-js: NodeJS"
    [:material-api:  `select`](https://pola-rs.github.io/nodejs-polars/interfaces/DataFrame-1.html#select) ·
    [:material-api:  `withColumns`](https://pola-rs.github.io/nodejs-polars/interfaces/DataFrame-1.html#withColumns)
    ``` javaScript
    --8<-- "getting-started/node/expressions.js:combine2"
    ```


```
shape: (8, 4)
┌─────┬──────────┬─────────────────────┬──────────┐
│ a   ┆ b        ┆ c                   ┆ a * b    │
│ --- ┆ ---      ┆ ---                 ┆ ---      │
│ i64 ┆ f64      ┆ datetime[μs]        ┆ f64      │
╞═════╪══════════╪═════════════════════╪══════════╡
│ 0   ┆ 0.220182 ┆ 2022-12-01 00:00:00 ┆ 0.0      │
├╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┤
│ 1   ┆ 0.750839 ┆ 2022-12-02 00:00:00 ┆ 0.750839 │
├╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┤
│ 2   ┆ 0.634639 ┆ 2022-12-03 00:00:00 ┆ 1.269277 │
├╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┤
│ 3   ┆ 0.67404  ┆ 2022-12-04 00:00:00 ┆ 2.022121 │
├╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┤
│ 4   ┆ 0.102818 ┆ 2022-12-05 00:00:00 ┆ 0.41127  │
├╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┤
│ 5   ┆ 0.896408 ┆ 2022-12-06 00:00:00 ┆ 4.482038 │
├╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┤
│ 6   ┆ 0.062943 ┆ 2022-12-07 00:00:00 ┆ 0.377657 │
├╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┤
│ 7   ┆ 0.108093 ┆ 2022-12-08 00:00:00 ┆ 0.756653 │
└─────┴──────────┴─────────────────────┴──────────┘
```
