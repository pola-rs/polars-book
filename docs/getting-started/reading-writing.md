# Reading & Writing

Polars supports reading & writing to all common files (e.g. csv, json, parquet), cloud storage (S3, Azure Blob, BigQuery) and databases (e.g. postgres, mysql). In the following examples we will show how to operate on most common file formats. For the following dataframe

=== ":fontawesome-brands-python: Python"
    [:material-api:  `DataFrame`](https://pola-rs.github.io/polars/py-polars/html/reference/dataframe/index.html)
    ``` python
    df = pl.DataFrame({"integer": [1, 2, 3,], 
                            "date": [
                                datetime(2022, 1, 1), 
                                datetime(2022, 1, 2), 
                                datetime(2022, 1, 3), 
                            ], 
                            "float":[4.0, 5.0, 6.0]})

    print(df)
    ```

=== ":fontawesome-brands-rust: Rust"
    [:material-api:  `DataFrame`](https://pola-rs.github.io/polars/polars/frame/struct.DataFrame.html)
    ``` rust
    let df: DataFrame = df!("integer" => &[1, 2, 3],
                            "date" => &[
                                        NaiveDate::from_ymd_opt(2022, 1, 1).unwrap().and_hms_opt(0, 0, 0).unwrap(),
                                        NaiveDate::from_ymd_opt(2022, 1, 2).unwrap().and_hms_opt(0, 0, 0).unwrap(),
                                        NaiveDate::from_ymd_opt(2022, 1, 3).unwrap().and_hms_opt(0, 0, 0).unwrap(),
                            ],
                            "float" => &[4.0, 5.0, 6.0]
                            ).expect("should not fail");
    println!("{}",df);
    ```
=== ":fontawesome-brands-node-js: NodeJS"
    [:material-api:  `DataFrame`](https://pola-rs.github.io/nodejs-polars/interfaces/DataFrame-1.html)
    ``` javaScript
    let df = pl.DataFrame({"integer": [1, 2, 3], 
                            "date": [
                                new Date(2022, 1, 1, 0, 0), 
                                new Date(2022, 1, 2, 0, 0), 
                                new Date(2022, 1, 3, 0, 0)
                            ], 
                            "float":[4.0, 5.0, 6.0]})
    console.log(df);
    ```


### CSV

Polars has its own fast implementation for csv reading with many flexible configuration options. 

=== ":fontawesome-brands-python: Python"
    [:material-api:  `read_csv`](https://pola-rs.github.io/polars/py-polars/html/reference/api/polars.read_csv.html) ·
    [:material-api:  `write_csv`](https://pola-rs.github.io/polars/py-polars/html/reference/api/polars.DataFrame.write_csv.html) 
    ``` python
    df.write_csv('output.csv')
    df_csv = pl.read_csv('output.csv')
    print(df_csv)
    ```

=== ":fontawesome-brands-rust: Rust"
    [:material-api:  `CsvReader`](https://pola-rs.github.io/polars/polars_io/csv/struct.CsvReader.html) ·
    [:material-api:  `CsvWriter`](https://pola-rs.github.io/polars/polars_io/csv/struct.CsvWriter.html) 
    ``` rust
    let mut file = File::create("output.csv").expect("could not create file");
    CsvWriter::new(&mut file).has_header(true).with_delimiter(b',').finish(&mut df);
    let df_csv = CsvReader::from_path("output.csv").unwrap().infer_schema(None).has_header(true).finish().unwrap();
    println!("{}",df_csv);
    ```
=== ":fontawesome-brands-node-js: NodeJS"
    [:material-api:  `readCSV`](https://pola-rs.github.io/nodejs-polars/functions/readCSV.html) ·
    [:material-api:  `writeCSV`](https://pola-rs.github.io/nodejs-polars/interfaces/DataFrame-1.html#writeCSV) 
    ``` javaScript
    df.writeCSV("output.csv");
    let df_csv = pl.readCSV("output.csv);
    console.log(df_csv);
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
    df_csv = pl.read_csv('output.csv',try_parse_dates=True)
    print(df_csv)
    ```

=== ":fontawesome-brands-rust: Rust"
    [:material-api:  `CsvReader`](https://pola-rs.github.io/polars/polars_io/csv/struct.CsvReader.html)
    ``` rust
    let mut file = File::create("output.csv").expect("could not create file");
    CsvWriter::new(&mut file).has_header(true).with_delimiter(b',').finish(&mut df);
    let df_csv = CsvReader::from_path("output.csv").unwrap().infer_schema(None).has_header(true).with_parse_dates(true).finish().unwrap();
    println!("{}",df_csv);
    ```
=== ":fontawesome-brands-node-js: NodeJS"
    [:material-api:  `readCSV`](https://pola-rs.github.io/nodejs-polars/functions/readCSV.html) ·
    ``` javaScript
    let df_csv = pl.readCSV("output.csv,{parseDates:true});
    console.log(df_csv);
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
    df.write_json('output.json')
    df_json = pl.read_json('output.json')
    print(df_json)
    ```

=== ":fontawesome-brands-rust: Rust"
    [:material-api:  `JsonReader`](https://pola-rs.github.io/polars/polars_io/json/struct.JsonReader.html) ·
    [:material-api:  `JsonWriter`](https://pola-rs.github.io/polars/polars_io/json/struct.JsonWriter.html)

    ``` rust
    let mut file = File::create("output.json").expect("could not create file");
    JsonWriter::new(&mut file).finish(&mut df);
    let mut f = File::open("output.json").unwrap();
    let df_json = JsonReader::new(f).with_json_format(JsonFormat::JsonLines).finish().unwrap();
    println!("{}",df_json);
    ```
=== ":fontawesome-brands-node-js: NodeJS"
    [:material-api:  `readJSON`](https://pola-rs.github.io/nodejs-polars/functions/readJSON.html) ·
    [:material-api:  `writeJSON`](https://pola-rs.github.io/nodejs-polars/interfaces/DataFrame-1.html#writeJSON) 
    ``` javaScript
    df.writeJSON("output.json");
    let df_json = pl.readJSON("output.json");
    console.log(df_json);
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
    df.write_parquet('output.parquet')
    df_parquet = pl.read_parquet('output.parquet')
    print(df_parquet)
    ```

=== ":fontawesome-brands-rust: Rust"
    [:material-api:  `ParquetReader`](https://pola-rs.github.io/polars/polars_io/parquet/struct.ParquetReader.html) ·
    [:material-api:  `ParquetWriter`](https://pola-rs.github.io/polars/polars_io/parquet/struct.ParquetWriter.html)
    ``` rust
    let mut file = File::create("output.parquet").expect("could not create file");
    ParquetWriter::new(&mut file).finish(&mut df);
    let mut f = File::open("output.parquet").unwrap();
    let df_parquet = ParquetReader::new(f).finish().unwrap();
    println!("{}",df_parquet);
    ```
=== ":fontawesome-brands-node-js: NodeJS"
    [:material-api:  `readParquet`](https://pola-rs.github.io/nodejs-polars/functions/readParquet.html) ·
    [:material-api:  `writeParquet`](https://pola-rs.github.io/nodejs-polars/interfaces/DataFrame-1.html#writeParquet) 
    ``` javaScript
    df.writeParquet("output.parquet");
    let df_parquet = pl.readParquet("output.parquet");
    console.log(df_parquet);
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
