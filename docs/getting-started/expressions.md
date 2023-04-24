# Expressions

`Expressions` are the core strength of `Polars`. The `expressions` offer a versatile structure that both solves easy queries and is easily extended to complex ones. Below we will cover the basic components that serve as building block (or in `Polars` terminology contexts) for all your queries:

- `select`
- `filter`
- `with_columns`
- `groupby`

To learn more about expressions and the context in which they operate, see the User Guide sections: [Contexts](../user-guide/concepts/contexts.md) and [Expressions](../user-guide/concepts/expressions.md).

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

```python exec="on" result="text" session="getting-started/expressions"
--8<-- "getting-started/python/expressions.py:setup"
print(
    --8<-- "getting-started/python/expressions.py:select"
)
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

```python exec="on" result="text" session="getting-started/expressions"
print(
    --8<-- "getting-started/python/expressions.py:select2"
)
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

```python exec="on" result="text" session="getting-started/expressions"
print(
    --8<-- "getting-started/python/expressions.py:select3"
)
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

```python exec="on" result="text" session="getting-started/expressions"
print(
    --8<-- "getting-started/python/expressions.py:exclude"
)
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

```python exec="on" result="text" session="getting-started/expressions"
print(
    --8<-- "getting-started/python/expressions.py:filter"
)
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

```python exec="on" result="text" session="getting-started/expressions"
print(
    --8<-- "getting-started/python/expressions.py:filter2"
)
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

```python exec="on" result="text" session="getting-started/expressions"
print(
    --8<-- "getting-started/python/expressions.py:with_columns"
)
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

```python exec="on" result="text" session="getting-started/expressions"
--8<-- "getting-started/python/expressions.py:dataframe2"
print(df2)
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

```python exec="on" result="text" session="getting-started/expressions"
print(
    --8<-- "getting-started/python/expressions.py:groupby"
)
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

```python exec="on" result="text" session="getting-started/expressions"
print(
    --8<-- "getting-started/python/expressions.py:groupby2"
)    
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

```python exec="on" result="text" session="getting-started/expressions"
--8<-- "getting-started/python/expressions.py:combine"
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


```python exec="on" result="text" session="getting-started/expressions"
--8<-- "getting-started/python/expressions.py:combine2"
```
