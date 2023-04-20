# Parsing

Polars has native support for parsing time series data and doing more sophisticated operations such as temporal grouping and resampling.

## Datatypes

`Polars` has the following datetime datatypes:

- `Date`: Date representation e.g. 2014-07-08. It is internally represented as days since UNIX epoch encoded by a 32-bit signed integer.
- `Datetime`: Datetime representation e.g. 2014-07-08 07:00:00. It is internally represented as a 64 bit integer since the Unix epoch and can have different units such as ns, us, ms.
- `Duration`: A time delta type that is created when subtracting `Date/Datetime`. Similar to `timedelta` in python.
- `Time`: Time representation, internally represented as nanoseconds since midnight.

## Parsing dates from a file

When loading from a CSV file `Polars` attempts to parse dates and times if the `try_parse_dates` flag is set to `True`:

=== ":fontawesome-brands-python: Python"
    ``` python
    --8<-- "user-guide/python/transformations/time-series/parsing.py:df"
    ```

```text
shape: (100, 2)
┌────────────┬────────┐
│ Date       ┆ Close  │
│ ---        ┆ ---    │
│ date       ┆ f64    │
╞════════════╪════════╡
│ 1981-02-23 ┆ 24.62  │
│ 1981-05-06 ┆ 27.38  │
│ 1981-05-18 ┆ 28.0   │
│ 1981-09-25 ┆ 14.25  │
│ …          ┆ …      │
│ 2012-12-04 ┆ 575.85 │
│ 2013-07-05 ┆ 417.42 │
│ 2013-11-07 ┆ 512.49 │
│ 2014-02-25 ┆ 522.06 │
└────────────┴────────┘
```

On the other hand binary formats such as parquet have a schema that is respected by `Polars`.

## Casting strings to dates

You can also cast a column of datetimes encoded as strings to a datetime type. You do this by calling the string `str.strptime` method and passing the format of the date string:

=== ":fontawesome-brands-python: Python"
    ``` python
    --8<-- "user-guide/python/transformations/time-series/parsing.py:cast"
    ```

```text
shape: (100, 2)
┌────────────┬────────┐
│ Date       ┆ Close  │
│ ---        ┆ ---    │
│ date       ┆ f64    │
╞════════════╪════════╡
│ 1981-02-23 ┆ 24.62  │
│ 1981-05-06 ┆ 27.38  │
│ 1981-05-18 ┆ 28.0   │
│ 1981-09-25 ┆ 14.25  │
│ …          ┆ …      │
│ 2012-12-04 ┆ 575.85 │
│ 2013-07-05 ┆ 417.42 │
│ 2013-11-07 ┆ 512.49 │
│ 2014-02-25 ┆ 522.06 │
└────────────┴────────┘
```

[The strptime date formats can be found here.](https://docs.rs/chrono/latest/chrono/format/strftime/index.html).

## Extracting date features from a date column

You can extract data features such as the year or day from a date column using the `.dt` namespace on a date column:

=== ":fontawesome-brands-python: Python"
    ``` python
    --8<-- "user-guide/python/transformations/time-series/parsing.py:extract"
    ```

```text
shape: (100, 3)
┌────────────┬────────┬──────┐
│ Date       ┆ Close  ┆ year │
│ ---        ┆ ---    ┆ ---  │
│ date       ┆ f64    ┆ i32  │
╞════════════╪════════╪══════╡
│ 1981-02-23 ┆ 24.62  ┆ 1981 │
│ 1981-05-06 ┆ 27.38  ┆ 1981 │
│ 1981-05-18 ┆ 28.0   ┆ 1981 │
│ 1981-09-25 ┆ 14.25  ┆ 1981 │
│ …          ┆ …      ┆ …    │
│ 2012-12-04 ┆ 575.85 ┆ 2012 │
│ 2013-07-05 ┆ 417.42 ┆ 2013 │
│ 2013-11-07 ┆ 512.49 ┆ 2013 │
│ 2014-02-25 ┆ 522.06 ┆ 2014 │
└────────────┴────────┴──────┘
```

## Mixed offsets

If you have mixed offsets (say, due to crossing daylight saving time),
then you can use `utc=True` and then convert to your time zone:

=== ":fontawesome-brands-python: Python"
    ``` python
    --8<-- "user-guide/python/transformations/time-series/parsing.py:mixed"
    ```
```text
shape: (4,)
Series: '' [datetime[μs, Europe/Brussels]]
[
    2021-03-27 00:00:00 CET
    2021-03-28 00:00:00 CET
    2021-03-29 00:00:00 CEST
    2021-03-30 00:00:00 CEST
]
```