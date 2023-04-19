# Data Structures

The core base data structures provided by Polars are  `Series` and `DataFrames`. 

## Series

Series are a 1-dimensional data structure. Within a series all elements have the same [Data Type](data-types.md) . 
The snippet below shows how to create a simple named `Series` object. 

=== ":fontawesome-brands-python: Python"
    [:material-api:  `Series`](https://pola-rs.github.io/polars/py-polars/html/reference/series/index.html)
    ``` python
    --8<-- "getting-started/python/series-dataframes.py:series"
    ```

=== ":fontawesome-brands-rust: Rust"
    [:material-api:  `Series`](https://pola-rs.github.io/polars/polars/series/struct.Series.html)
    ``` rust
    --8<-- "getting-started/rust/series-dataframes.rs:series"
    ```
=== ":fontawesome-brands-node-js: NodeJS"
    [:material-api:  `Series`](https://pola-rs.github.io/nodejs-polars/interfaces/Series-1.html)
    ``` javaScript
    --8<-- "getting-started/node/series-dataframes.js:series"
    ```

```
shape: (5,)
Series: 'a' [i64]
[
    1
    2
    3
    4
    5
]
```

## DataFrame

A `DataFrame` is a 2-dimensional data structure that is backed by a `Series`, and it could be seen as an abstraction of on collection (e.g. list) of `Series`. Operations that can be executed on `DataFrame` are very similar to what is done in a `SQL` like query. You can `GROUP BY`, `JOIN`, `PIVOT`, but also define custom functions.

=== ":fontawesome-brands-python: Python"
    [:material-api:  `DataFrame`](https://pola-rs.github.io/polars/py-polars/html/reference/dataframe/index.html)
    ``` python
    --8<-- "getting-started/python/series-dataframes.py:dataframe"
    ```

=== ":fontawesome-brands-rust: Rust"
    [:material-api:  `DataFrame`](https://pola-rs.github.io/polars/polars/frame/struct.DataFrame.html)
    ``` rust
    --8<-- "getting-started/rust/series-dataframes.rs:dataframe"
    ```
=== ":fontawesome-brands-node-js: NodeJS"
    [:material-api:  `DataFrame`](https://pola-rs.github.io/nodejs-polars/interfaces/DataFrame-1.html)
    ``` javaScript
    --8<-- "getting-started/node/series-dataframes.js:dataframe"
    ```

```
shape: (3, 3)
┌─────────┬─────────────────────┬───────┐
│ integer ┆ date                ┆ float │
│ ---     ┆ ---                 ┆ ---   │
│ i64     ┆ datetime[μs]        ┆ f64   │
╞═════════╪═════════════════════╪═══════╡
│ 1       ┆ 2022-01-01 00:00:00 ┆ 4.0   │
├╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌┤
│ 2       ┆ 2022-01-02 00:00:00 ┆ 5.0   │
├╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌┤
│ 3       ┆ 2022-01-03 00:00:00 ┆ 6.0   │
├╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌┤
│ 4       ┆ 2022-01-04 00:00:00 ┆ 7.0   │
├╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌┤
│ 5       ┆ 2022-01-05 00:00:00 ┆ 8.0   │
└─────────┴─────────────────────┴───────┘

```

### Viewing data

This part focuses on viewing data in a `DataFrame`. We will use the `DataFrame` from the previous example as a starting point.

#### Head

The `head` function shows by default the first 5 rows of a `DataFrame`. You can specify the number of rows you want to see (e.g. `df.head(10)`).

=== ":fontawesome-brands-python: Python"
    [:material-api:  `head`](https://pola-rs.github.io/polars/polars/frame/struct.DataFrame.html#method.head)
    ``` python
    --8<-- "getting-started/python/series-dataframes.py:head"
    ```

=== ":fontawesome-brands-rust: Rust"
    [:material-api:  `head`](https://pola-rs.github.io/polars/py-polars/html/reference/dataframe/api/polars.DataFrame.head.html)
    ``` rust
    --8<-- "getting-started/rust/series-dataframes.rs:head"
    ```
=== ":fontawesome-brands-node-js: NodeJS"
    [:material-api:  `head`](https://pola-rs.github.io/nodejs-polars/interfaces/DataFrame-1.html#head)
    ``` javaScript
    --8<-- "getting-started/node/series-dataframes.js:head"
    ```


```
shape: (3, 3)
┌─────────┬─────────────────────┬───────┐
│ integer ┆ date                ┆ float │
│ ---     ┆ ---                 ┆ ---   │
│ i64     ┆ datetime[μs]        ┆ f64   │
╞═════════╪═════════════════════╪═══════╡
│ 1       ┆ 2022-01-01 00:00:00 ┆ 4.0   │
├╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌┤
│ 2       ┆ 2022-01-02 00:00:00 ┆ 5.0   │
├╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌┤
│ 3       ┆ 2022-01-03 00:00:00 ┆ 6.0   │
└─────────┴─────────────────────┴───────┘
```

#### Tail

The `tail` function shows the last 5 rows of a `DataFrame`. You can also specify the number of rows you want to see, similar to `head`.

=== ":fontawesome-brands-python: Python"
    [:material-api:  `tail`](https://pola-rs.github.io/polars/py-polars/html/reference/dataframe/api/polars.DataFrame.tail.html)
    ``` python
    --8<-- "getting-started/python/series-dataframes.py:tail"
    ```

=== ":fontawesome-brands-rust: Rust"
    [:material-api:  `tail`](https://pola-rs.github.io/polars/polars/frame/struct.DataFrame.html#method.tail)
    ``` rust
    --8<-- "getting-started/rust/series-dataframes.rs:tail"
    ```
=== ":fontawesome-brands-node-js: NodeJS"
    [:material-api:  `tail`](https://pola-rs.github.io/nodejs-polars/interfaces/DataFrame-1.html#tail)
    ``` javaScript
    --8<-- "getting-started/node/series-dataframes.js:tail"
    ```

```
shape: (3, 3)
┌─────────┬─────────────────────┬───────┐
│ integer ┆ date                ┆ float │
│ ---     ┆ ---                 ┆ ---   │
│ i64     ┆ datetime[μs]        ┆ f64   │
╞═════════╪═════════════════════╪═══════╡
│ 3       ┆ 2022-01-03 00:00:00 ┆ 6.0   │
├╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌┤
│ 4       ┆ 2022-01-04 00:00:00 ┆ 7.0   │
├╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌┤
│ 5       ┆ 2022-01-05 00:00:00 ┆ 8.0   │
└─────────┴─────────────────────┴───────┘
```

#### Sample

If you want to get an impression of the data of your `DataFrame`, you can also use `sample`. With `sample` you get an *n* number of random rows from the `DataFrame`.

=== ":fontawesome-brands-python: Python"
    [:material-api:  `sample`](https://pola-rs.github.io/polars/py-polars/html/reference/dataframe/api/polars.DataFrame.sample.html)
    ``` python
    --8<-- "getting-started/python/series-dataframes.py:sample"
    ```

=== ":fontawesome-brands-rust: Rust"
    [:material-api:  `sample_n`](https://pola-rs.github.io/polars/polars/frame/struct.DataFrame.html#method.sample_n)
    ``` rust
    --8<-- "getting-started/rust/series-dataframes.rs:sample"
    ```
=== ":fontawesome-brands-node-js: NodeJS"
    [:material-api:  `sample`](https://pola-rs.github.io/nodejs-polars/interfaces/DataFrame-1.html#sample)
    ``` javaScript
    --8<-- "getting-started/node/series-dataframes.js:sample"
    ```

```
shape: (2, 3)
┌─────────┬─────────────────────┬───────┐
│ integer ┆ date                ┆ float │
│ ---     ┆ ---                 ┆ ---   │
│ f64     ┆ datetime[ms]        ┆ f64   │
╞═════════╪═════════════════════╪═══════╡
│ 1.0     ┆ 2022-01-31 23:00:00 ┆ 4.0   │
├╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌┤
│ 2.0     ┆ 2022-02-01 23:00:00 ┆ 5.0   │
└─────────┴─────────────────────┴───────┘
```

#### Describe

`Describe` returns summary statistics of your `DataFrame`. It will provide several quick statistics if possible.

=== ":fontawesome-brands-python: Python"
    [:material-api:  `describe`](https://pola-rs.github.io/polars/py-polars/html/reference/dataframe/api/polars.DataFrame.describe.html)
    ``` python
    --8<-- "getting-started/python/series-dataframes.py:describe"
    ```

=== ":fontawesome-brands-rust: Rust"
    [:material-api:  `describe`](https://pola-rs.github.io/polars/polars/frame/struct.DataFrame.html#method.describe)
    ``` rust
    --8<-- "getting-started/rust/series-dataframes.rs:describe"
    ```
=== ":fontawesome-brands-node-js: NodeJS"
    [:material-api:  `describe`](https://pola-rs.github.io/nodejs-polars/interfaces/DataFrame-1.html#describe)
    ``` javaScript
    --8<-- "getting-started/node/series-dataframes.js:describe"
    ```

```
shape: (5, 4)
┌──────────┬─────────┬─────────────────────┬───────┐
│ describe ┆ integer ┆ date                ┆ float │
│ ---      ┆ ---     ┆ ---                 ┆ ---   │
│ str      ┆ f64     ┆ datetime[ms]        ┆ f64   │
╞══════════╪═════════╪═════════════════════╪═══════╡
│ mean     ┆ 2.0     ┆ null                ┆ 5.0   │
├╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌┤
│ std      ┆ 1.0     ┆ null                ┆ 1.0   │
├╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌┤
│ min      ┆ 1.0     ┆ 2022-01-31 23:00:00 ┆ 4.0   │
├╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌┤
│ max      ┆ 3.0     ┆ 2022-02-02 23:00:00 ┆ 6.0   │
├╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌┤
│ median   ┆ 2.0     ┆ null                ┆ 5.0   │
└──────────┴─────────┴─────────────────────┴───────┘
```