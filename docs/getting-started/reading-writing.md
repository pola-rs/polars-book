# Reading & Writing

Polars supports reading & writing to all common files (e.g. csv, json, parquet), cloud storage (S3, Azure Blob, BigQuery) and databases (e.g. postgres, mysql). In the following examples we will show how to operate on most common file formats. For the following dataframe

=== ":fontawesome-brands-python: Python"
    [:material-api:  `DataFrame`](https://pola-rs.github.io/polars/py-polars/html/reference/dataframe/index.html)
    ``` python
    --8<-- "getting-started/python/reading-writing.py:dataframe"
    ```

=== ":fontawesome-brands-rust: Rust"
    [:material-api:  `DataFrame`](https://pola-rs.github.io/polars/polars/frame/struct.DataFrame.html)
    ``` rust
    --8<-- "getting-started/rust/reading-writing.rs:dataframe"
    ```
=== ":fontawesome-brands-node-js: NodeJS"
    [:material-api:  `DataFrame`](https://pola-rs.github.io/nodejs-polars/interfaces/DataFrame-1.html)
    ``` javaScript
    --8<-- "getting-started/node/reading-writing.js:dataframe"
    ```


#### CSV

Polars has its own fast implementation for csv reading with many flexible configuration options. 

=== ":fontawesome-brands-python: Python"
    [:material-api:  `read_csv`](https://pola-rs.github.io/polars/py-polars/html/reference/api/polars.read_csv.html) ·
    [:material-api:  `write_csv`](https://pola-rs.github.io/polars/py-polars/html/reference/api/polars.DataFrame.write_csv.html) 
    ``` python
    --8<-- "getting-started/python/reading-writing.py:csv"
    ```

=== ":fontawesome-brands-rust: Rust"
    [:material-api:  `CsvReader`](https://pola-rs.github.io/polars/polars_io/csv/struct.CsvReader.html) ·
    [:material-api:  `CsvWriter`](https://pola-rs.github.io/polars/polars_io/csv/struct.CsvWriter.html) 
    ``` rust
    --8<-- "getting-started/rust/reading-writing.rs:csv"
    ```
=== ":fontawesome-brands-node-js: NodeJS"
    [:material-api:  `readCSV`](https://pola-rs.github.io/nodejs-polars/functions/readCSV.html) ·
    [:material-api:  `writeCSV`](https://pola-rs.github.io/nodejs-polars/interfaces/DataFrame-1.html#writeCSV) 
    ``` javaScript
    --8<-- "getting-started/node/reading-writing.js:csv"
    ```

```
shape: (3, 3)
┌─────────┬────────────────────────────┬───────┐
│ integer ┆ date                       ┆ float │
│ ---     ┆ ---                        ┆ ---   │
│ i64     ┆ str                        ┆ f64   │
╞═════════╪════════════════════════════╪═══════╡
│ 1       ┆ 2022-01-01T00:00:00.000000 ┆ 4.0   │
├╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌┤
│ 2       ┆ 2022-01-02T00:00:00.000000 ┆ 5.0   │
├╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌┤
│ 3       ┆ 2022-01-03T00:00:00.000000 ┆ 6.0   │
└─────────┴────────────────────────────┴───────┘
```

As we can see above, Polars made the datetimes a `string`. We can tell Polars to parse dates, when reading the csv, to ensure the date becomes a datetime. The example can be found below:

=== ":fontawesome-brands-python: Python"
    [:material-api:  `read_csv`](https://pola-rs.github.io/polars/py-polars/html/reference/api/polars.read_csv.html)
    ``` python
    --8<-- "getting-started/python/reading-writing.py:csv2"
    ```

=== ":fontawesome-brands-rust: Rust"
    [:material-api:  `CsvReader`](https://pola-rs.github.io/polars/polars_io/csv/struct.CsvReader.html)
    ``` rust
    --8<-- "getting-started/rust/reading-writing.rs:csv2"
    ```
=== ":fontawesome-brands-node-js: NodeJS"
    [:material-api:  `readCSV`](https://pola-rs.github.io/nodejs-polars/functions/readCSV.html) ·
    ``` javaScript
    --8<-- "getting-started/node/reading-writing.js:csv2"
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

#### JSON

=== ":fontawesome-brands-python: Python"
    [:material-api:  `read_json`](https://pola-rs.github.io/polars/py-polars/html/reference/api/polars.read_json.html) ·
    [:material-api:  `write_csv`](https://pola-rs.github.io/polars/py-polars/html/reference/api/polars.DataFrame.write_json.html) 
    ``` python
    --8<-- "getting-started/python/reading-writing.py:json"
    ```

=== ":fontawesome-brands-rust: Rust"
    [:material-api:  `JsonReader`](https://pola-rs.github.io/polars/polars_io/json/struct.JsonReader.html) ·
    [:material-api:  `JsonWriter`](https://pola-rs.github.io/polars/polars_io/json/struct.JsonWriter.html)

    ``` rust
    --8<-- "getting-started/rust/reading-writing.rs:json"
    ```
=== ":fontawesome-brands-node-js: NodeJS"
    [:material-api:  `readJSON`](https://pola-rs.github.io/nodejs-polars/functions/readJSON.html) ·
    [:material-api:  `writeJSON`](https://pola-rs.github.io/nodejs-polars/interfaces/DataFrame-1.html#writeJSON) 
    ``` javaScript
    --8<-- "getting-started/node/reading-writing.js:json"
    ```

```
shape: (3, 3)
┌─────────┬─────────────────────┬───────┐
│ integer ┆ date                ┆ float │
│ ---     ┆ ---                 ┆ ---   │
│ i64     ┆ str                 ┆ f64   │
╞═════════╪═════════════════════╪═══════╡
│ 1       ┆ 2022-01-01 00:00:00 ┆ 4.0   │
├╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌┤
│ 2       ┆ 2022-01-02 00:00:00 ┆ 5.0   │
├╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌┤
│ 3       ┆ 2022-01-03 00:00:00 ┆ 6.0   │
└─────────┴─────────────────────┴───────┘
```

#### Parquet

=== ":fontawesome-brands-python: Python"
    [:material-api:  `read_parquet`](https://pola-rs.github.io/polars/py-polars/html/reference/api/polars.read_parquet.html) ·
    [:material-api:  `write_parquet`](https://pola-rs.github.io/polars/py-polars/html/reference/api/polars.DataFrame.write_parquet.html) 
    ``` python
    --8<-- "getting-started/python/reading-writing.py:parquet"
    ```

=== ":fontawesome-brands-rust: Rust"
    [:material-api:  `ParquetReader`](https://pola-rs.github.io/polars/polars_io/parquet/struct.ParquetReader.html) ·
    [:material-api:  `ParquetWriter`](https://pola-rs.github.io/polars/polars_io/parquet/struct.ParquetWriter.html)
    ``` rust
    --8<-- "getting-started/rust/reading-writing.rs:parquet"
    ```
=== ":fontawesome-brands-node-js: NodeJS"
    [:material-api:  `readParquet`](https://pola-rs.github.io/nodejs-polars/functions/readParquet.html) ·
    [:material-api:  `writeParquet`](https://pola-rs.github.io/nodejs-polars/interfaces/DataFrame-1.html#writeParquet) 
    ``` javaScript
    --8<-- "getting-started/node/reading-writing.js:parquet"
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