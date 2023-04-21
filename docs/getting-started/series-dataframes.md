# Series & DataFrames

The core base data structures provided by Polars are  `Series` and `DataFrames`. 

## Series

Series are a 1-dimensional data structure. Within a series all elements have the same data type (e.g. int, string). 
The snippet below shows how to create a simple named `Series` object. In a later section of this getting started guide we will learn how to read data from external sources (e.g. files, database), for now lets keep it simple.   

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

```python exec="on" result="text" session="getting-started/series"
--8<-- "getting-started/python/series-dataframes.py:series"
```

### Methods

Although it is more common to work directly on a `DataFrame` object, `Series` implement a number of base methods which make it easy to perform transformations. Below are some examples of common operations you might want to perform. Note that these are for illustration purposes and only show a small subset of what is available.


##### Aggregations

`Series` out of the box supports all basic aggregations (e.g. min, max, mean, mode, ...).

=== ":fontawesome-brands-python: Python"
    [:material-api:  `min`](https://pola-rs.github.io/polars/py-polars/html/reference/series/api/polars.Series.min.html) ·
    [:material-api:  `max`](https://pola-rs.github.io/polars/py-polars/html/reference/series/api/polars.Series.max.html)
    ``` python
    --8<-- "getting-started/python/series-dataframes.py:minmax"
    ```

=== ":fontawesome-brands-rust: Rust"
    [:material-api:  `min`](https://pola-rs.github.io/polars/polars/series/struct.Series.html#method.min) ·
    [:material-api:  `max`](https://pola-rs.github.io/polars/polars/series/struct.Series.html#method.max)
    ``` rust
    --8<-- "getting-started/rust/series-dataframes.rs:minmax"
    ```
=== ":fontawesome-brands-node-js: NodeJS"
    [:material-api:  `min`](https://pola-rs.github.io/nodejs-polars/interfaces/Series-1.html#min) ·
    [:material-api:  `max`](https://pola-rs.github.io/nodejs-polars/interfaces/Series-1.html#max)
    ``` javaScript
    --8<-- "getting-started/node/series-dataframes.js:minmax"
    ```

```python exec="on" result="text" session="getting-started/series"
--8<-- "getting-started/python/series-dataframes.py:minmax"
```

##### String

There are a number of methods related to string operations in the `StringNamespace`. These only work on `Series` with the Datatype `Utf8`.

=== ":fontawesome-brands-python: Python"
    [:material-api:  `replace`](https://pola-rs.github.io/polars/py-polars/html/reference/series/api/polars.Series.str.replace.html)
    ``` python
    --8<-- "getting-started/python/series-dataframes.py:string"
    ```

=== ":fontawesome-brands-rust: Rust"
    ``` rust
    --8<-- "getting-started/rust/series-dataframes.rs:string"
    ```
=== ":fontawesome-brands-node-js: NodeJS"
    [:material-api:  `replace`](https://pola-rs.github.io/nodejs-polars/interfaces/StringNamespace.html#replace)
    ``` javaScript
    --8<-- "getting-started/node/series-dataframes.js:string"
    ```

```python exec="on" result="text" session="getting-started/series"
--8<-- "getting-started/python/series-dataframes.py:string"
```

##### Datetime

Similar to strings, there is a seperate namespace for datetime related operations in the `DateLikeNameSpace`. These only work on `Series`with DataTypes related to dates.

=== ":fontawesome-brands-python: Python"
    [:material-api:  `day`](https://pola-rs.github.io/polars/py-polars/html/reference/series/api/polars.Series.dt.day.html)
    ``` python
    --8<-- "getting-started/python/series-dataframes.py:dt"
    ```

=== ":fontawesome-brands-rust: Rust"
    ``` rust
    --8<-- "getting-started/rust/series-dataframes.rs:dt"
    ```
=== ":fontawesome-brands-node-js: NodeJS"
    [:material-api:  `day`](https://pola-rs.github.io/nodejs-polars/interfaces/DatetimeNamespace.html#day)
    ``` javaScript
    --8<-- "getting-started/node/series-dataframes.js:dt"
    ```

```python exec="on" result="text" session="getting-started/series"
--8<-- "getting-started/python/series-dataframes.py:dt"
```

## DataFrame

A `DataFrame` is a 2-dimensional data structure that is backed by a `Series`, and it could be seen as an abstraction of on collection (e.g. list) of `Series`. Operations that can be executed on `DataFrame` are very similar to what is done in a `SQL` like query. You can `GROUP BY`, `JOIN`, `PIVOT`, but also define custom functions. In the next pages we will cover how to perform these transformations.

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

```python exec="on" result="text" session="getting-started/series"
--8<-- "getting-started/python/series-dataframes.py:dataframe"
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


```python exec="on" result="text" session="getting-started/series"
--8<-- "getting-started/python/series-dataframes.py:head"
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

```python exec="on" result="text" session="getting-started/series"
--8<-- "getting-started/python/series-dataframes.py:tail"
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

```python exec="on" result="text" session="getting-started/series"
--8<-- "getting-started/python/series-dataframes.py:sample"
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

```python exec="on" result="text" session="getting-started/series"
--8<-- "getting-started/python/series-dataframes.py:describe"
```
