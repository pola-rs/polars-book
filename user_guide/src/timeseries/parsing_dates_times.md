# Parsing dates and times

## Datatypes
`Polars` inherits the following datetime datatypes from Apache Arrow:
- `Date`: Date representation (e.g. 2014-07-08), internally represented as days since UNIX epoch encoded by a 32-bit signed integer.
- `Datetime`: Datetime representation (e.g. ), internally represented as nanoseconds since UNIX
  epoch encoded by a 64-bit signed integer.
- `Duration`: A timedelate type. Created when subtracting `Date/Datetime`.
- `Time`: Time representation, internally represented as nanoseconds since midnight.

## Parsing dates and times
When loading from a file `Polars` can attempt to parse dates and times if the `parse_dates` flag is set to `True`. 
```python
df = pl.read_csv("apple_stock.csv", parse_dates=True)
```
```
┌────────────┬───────┐
│ Date       ┆ Open  │
│ ---        ┆ ---   │
│ date       ┆ f64   │
╞════════════╪═══════╡
│ 2014-07-08 ┆ 96.27 │
├╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌┤
│ 2014-07-07 ┆ 94.14 │
├╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌┤
│ 2014-07-03 ┆ 93.67 │
└────────────┴───────┘
```
You can also cast a column of datetimes encoded as strings to a datetime type. You do this by calling the string `str.strptime` method and passing the format of the date string:
```python
df.with_column(pl.col('Date').str.strptime(pl.Date, fmt='%Y-%m-%d'))
```
This page [sets out the strptime date formats](https://docs.rs/chrono/latest/chrono/format/strftime/index.html).