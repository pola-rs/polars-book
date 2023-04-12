# Series & DataFrames

The core base data structures provided by Polars are  `Series` and `DataFrames`. 

## Series

Series are a 1-dimensional data structure. Within a series all elements have the same data type (e.g. int, string). 
The snippet below shows how to create a simple named `Series` object. In a later section of this getting started guide we will learn how to read data from external sources (e.g. files, database), for now lets keep it simple.   

=== ":fontawesome-brands-python: Python"
    [:material-api:  `Series`](https://pola-rs.github.io/polars/py-polars/html/reference/series/index.html)
    ``` python
    import polars as pl
    
    s = pl.Series("a", [1, 2, 3, 4, 5])
    print(s)
    ```

=== ":fontawesome-brands-rust: Rust"
    [:material-api:  `Series`](https://pola-rs.github.io/polars/polars/series/struct.Series.html)
    ``` rust
    use polars::prelude::*;

    let s = Series::new("a", [1, 2, 3, 4, 5]);
    println!("{}",s);
    ```
=== ":fontawesome-brands-node-js: NodeJS"
    [:material-api:  `Series`](https://pola-rs.github.io/nodejs-polars/interfaces/Series-1.html)
    ``` javaScript
    import pl from 'nodejs-polars';

    const s = pl.Series("a", [1, 2, 3, 4, 5]);
    console.log(s);
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

### Methods

Although it is more common to work directly on a `DataFrame` object, `Series` implement a number of base methods which make it easy to perform transformations. Below are some examples of common operations you might want to perform. Note that these are for illustration purposes and only show a small subset of what is available.


##### Aggregations

`Series` out of the box supports all basic aggregations (e.g. min, max, mean, mode, ...).

=== ":fontawesome-brands-python: Python"
    [:material-api:  `min`](https://pola-rs.github.io/polars/py-polars/html/reference/series/api/polars.Series.min.html) ·
    [:material-api:  `max`](https://pola-rs.github.io/polars/py-polars/html/reference/series/api/polars.Series.max.html)
    ``` python
    s = pl.Series("a", [1, 2, 3, 4, 5])
    print(s.min())
    print(s.max())
    ```

=== ":fontawesome-brands-rust: Rust"
    [:material-api:  `min`](https://pola-rs.github.io/polars/polars/series/struct.Series.html#method.min) ·
    [:material-api:  `max`](https://pola-rs.github.io/polars/polars/series/struct.Series.html#method.max)
    ``` rust
    let s = Series::new("a", [1, 2, 3, 4, 5]);
    // The use of generics is necessary for the type system
    println!("{}",s.min::<u64>().unwrap());
    println!("{}",s.max::<u64>().unwrap());
    ```
=== ":fontawesome-brands-node-js: NodeJS"
    [:material-api:  `min`](https://pola-rs.github.io/nodejs-polars/interfaces/Series-1.html#min) ·
    [:material-api:  `max`](https://pola-rs.github.io/nodejs-polars/interfaces/Series-1.html#max)
    ``` javaScript
    const s = pl.Series("a", [1, 2, 3, 4, 5]);
    console.log(s.min());
    console.log(s.max());
    ```

```
1
5
```

##### String

There are a number of methods related to string operations in the `StringNamespace`. These only work on `Series` with the Datatype `Utf8`.

=== ":fontawesome-brands-python: Python"
    [:material-api:  `replace`](https://pola-rs.github.io/polars/py-polars/html/reference/series/api/polars.Series.str.replace.html)
    ``` python
    s = pl.Series("a", ["polar", "bear","arctic" ,"polar fox", "polar bear"])
    s2 = s.str.replace("polar","pola")
    print(s2)
    ```

=== ":fontawesome-brands-rust: Rust"
    ``` rust
    // This operation is not directly available on the Series object yet, only on the DataFrame
    ```
=== ":fontawesome-brands-node-js: NodeJS"
    [:material-api:  `replace`](https://pola-rs.github.io/nodejs-polars/interfaces/StringNamespace.html#replace)
    ``` javaScript
    const s = pl.Series("a", ["polar", "bear","arctic" ,"polar fox", "polar bear"]);
    const s2 = s.str.replace("polar","pola");
    console.log(s2);
    ```

```
shape: (5,)
Series: '' [str]
[
    "pola"
    "bear"
    "arctic"
    "pola fox"
    "pola bear"
],
```

##### Datetime

Similar to strings, there is a seperate namespace for datetime related operations in the `DateLikeNameSpace`. These only work on `Series`with DataTypes related to dates.

=== ":fontawesome-brands-python: Python"
    [:material-api:  `day`](https://pola-rs.github.io/polars/py-polars/html/reference/series/api/polars.Series.dt.day.html)
    ``` python
    from datetime import datetime
    start = datetime(2001, 1, 1)
    stop = datetime(2001, 1, 9)
    s = pl.date_range(start, stop, interval="2d")
    s.dt.day()
    print(s)
    ```

=== ":fontawesome-brands-rust: Rust"
    ``` rust
    // This operation is not directly available on the Series object yet, only on the DataFrame
    ```
=== ":fontawesome-brands-node-js: NodeJS"
    [:material-api:  `day`](https://pola-rs.github.io/nodejs-polars/interfaces/DatetimeNamespace.html#day)
    ``` javaScript
    const s = pl.Series("a", [new Date(2001,1,1),new Date(2001,1,3),new Date(2001,1,5),new Date(2001,1,7),new Date(2001,1,9)]);
    const s2 = s.date.day();
    console.log(s2);
    ```

```
shape: (5,)
Series: '' [u32]
[
        1
        3
        5
        7
        9
]
```

## DataFrame

A `DataFrame` is a 2-dimensional data structure that is backed by a `Series`, and it could be seen as an abstraction of on collection (e.g. list) of `Series`. Operations that can be executed on `DataFrame` are very similar to what is done in a `SQL` like query. You can `GROUP BY`, `JOIN`, `PIVOT`, but also define custom functions. In the next pages we will cover how to perform these transformations.

=== ":fontawesome-brands-python: Python"
    [:material-api:  `DataFrame`](https://pola-rs.github.io/polars/py-polars/html/reference/dataframe/index.html)
    ``` python
    df = pl.DataFrame({"integer": [1, 2, 3, 4, 5], 
                            "date": [
                                datetime(2022, 1, 1), 
                                datetime(2022, 1, 2), 
                                datetime(2022, 1, 3), 
                                datetime(2022, 1, 4), 
                                datetime(2022, 1, 5)
                            ], 
                            "float":[4.0, 5.0, 6.0, 7.0, 8.0]})

    print(df)
    ```

=== ":fontawesome-brands-rust: Rust"
    [:material-api:  `DataFrame`](https://pola-rs.github.io/polars/polars/frame/struct.DataFrame.html)
    ``` rust
    let df: DataFrame = df!("integer" => &[1, 2, 3, 4, 5],
                            "date" => &[
                                        NaiveDate::from_ymd_opt(2022, 1, 1).unwrap().and_hms_opt(0, 0, 0).unwrap(),
                                        NaiveDate::from_ymd_opt(2022, 1, 2).unwrap().and_hms_opt(0, 0, 0).unwrap(),
                                        NaiveDate::from_ymd_opt(2022, 1, 3).unwrap().and_hms_opt(0, 0, 0).unwrap(),
                                        NaiveDate::from_ymd_opt(2022, 1, 4).unwrap().and_hms_opt(0, 0, 0).unwrap(),
                                        NaiveDate::from_ymd_opt(2022, 1, 5).unwrap().and_hms_opt(0, 0, 0).unwrap()
                            ],
                            "float" => &[4.0, 5.0, 6.0 7.0, 8.0]
                            ).expect("should not fail");
    println!("{}",df);
    ```
=== ":fontawesome-brands-node-js: NodeJS"
    [:material-api:  `DataFrame`](https://pola-rs.github.io/nodejs-polars/interfaces/DataFrame-1.html)
    ``` javaScript
    let df = pl.DataFrame({"integer": [1, 2, 3, 4, 5], 
                            "date": [
                                new Date(2022, 1, 1, 0, 0), 
                                new Date(2022, 1, 2, 0, 0), 
                                new Date(2022, 1, 3, 0, 0), 
                                new Date(2022, 1, 4, 0, 0), 
                                new Date(2022, 1, 5, 0, 0)
                            ], 
                            "float":[4.0, 5.0, 6.0, 7.0, 8.0]})
    console.log(df);
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
    print(df.head(3))
    ```

=== ":fontawesome-brands-rust: Rust"
    [:material-api:  `head`](https://pola-rs.github.io/polars/py-polars/html/reference/dataframe/api/polars.DataFrame.head.html)
    ``` rust
    println!("{}",df.head(Some(3)));
    ```
=== ":fontawesome-brands-node-js: NodeJS"
    [:material-api:  `head`](https://pola-rs.github.io/nodejs-polars/interfaces/DataFrame-1.html#head)
    ``` javaScript
    console.log(df.head(3));
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
    print(df.tail(3))
    ```

=== ":fontawesome-brands-rust: Rust"
    [:material-api:  `tail`](https://pola-rs.github.io/polars/polars/frame/struct.DataFrame.html#method.tail)
    ``` rust
    println!("{}",df.tail(Some(3)));
    ```
=== ":fontawesome-brands-node-js: NodeJS"
    [:material-api:  `tail`](https://pola-rs.github.io/nodejs-polars/interfaces/DataFrame-1.html#tail)
    ``` javaScript
    console.log(df.tail(3));
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
    print(df.sample(2))
    ```

=== ":fontawesome-brands-rust: Rust"
    [:material-api:  `sample_n`](https://pola-rs.github.io/polars/polars/frame/struct.DataFrame.html#method.sample_n)
    ``` rust
    println!("{}",df.sample_n(2, false, true, None).unwrap());
    ```
=== ":fontawesome-brands-node-js: NodeJS"
    [:material-api:  `sample`](https://pola-rs.github.io/nodejs-polars/interfaces/DataFrame-1.html#sample)
    ``` javaScript
    console.log(df.sample(2));
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
    print(df.describe())
    ```

=== ":fontawesome-brands-rust: Rust"
    [:material-api:  `describe`](https://pola-rs.github.io/polars/polars/frame/struct.DataFrame.html#method.describe)
    ``` rust
    println!("{}",df.describe(None));
    ```
=== ":fontawesome-brands-node-js: NodeJS"
    [:material-api:  `describe`](https://pola-rs.github.io/nodejs-polars/interfaces/DataFrame-1.html#describe)
    ``` javaScript
    console.log(df.describe());
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
