# Filtering date columns

Filtering by dates works in the same way as with other types of columns using the `.filter` method.

In the following example we use a time series of Apple stock prices.

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

## Filtering by single dates

We can filter by a single date by casting the desired date string to a `Date` object
in a filter expression:

```python
df.filter(pl.col("Date") == pl.datetime(2014, 7, 8))
```

Note we are using the lowercase `datetime` method rather than the `Datetime` data type.

## Filtering by a date range

We can filter by a range of dates using the `is_between` method in a filter expression:

```python
df.filter(pl.col("Date").is_between(pl.datetime(2014, 7, 1),pl.datetime(2018,8,1)))
```
