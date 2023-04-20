# Filtering

Filtering date columns works in the same way as with other types of columns using the `.filter` method.

Polars uses Python's native `datetime`, `date` and `timedelta` for equality comparisons between the datatypes `pl.Datetime`, `pl.Date` and `pl.Duration`.

In the following example we use a time series of Apple stock prices.

=== ":fontawesome-brands-python: Python"
    ``` python
    --8<-- "user-guide/python/transformations/time-series/filter.py:df"
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

## Filtering by single dates

We can filter by a single date by casting the desired date string to a `Date` object
in a filter expression:

=== ":fontawesome-brands-python: Python"
    ``` python
    --8<-- "user-guide/python/transformations/time-series/filter.py:filter"
    ```

```text
shape: (1, 2)
┌────────────┬───────┐
│ Date       ┆ Close │
│ ---        ┆ ---   │
│ date       ┆ f64   │
╞════════════╪═══════╡
│ 1995-10-16 ┆ 36.13 │
└────────────┴───────┘
```

Note we are using the lowercase `datetime` method rather than the uppercase `Datetime` data type.

## Filtering by a date range

We can filter by a range of dates using the `is_between` method in a filter expression with the start and end dates:

=== ":fontawesome-brands-python: Python"
    ``` python
    --8<-- "user-guide/python/transformations/time-series/filter.py:range"
    ```

```text
shape: (2, 2)
┌────────────┬───────┐
│ Date       ┆ Close │
│ ---        ┆ ---   │
│ date       ┆ f64   │
╞════════════╪═══════╡
│ 1995-07-06 ┆ 47.0  │
│ 1995-10-16 ┆ 36.13 │
└────────────┴───────┘
```

## Filtering with negative dates

Say you are working with an archeologist and are dealing in negative dates.
Polars can parse and store them just fine, but the Python `datetime` library
does not. So for filtering, you should use attributes in the `.dt` namespace:

=== ":fontawesome-brands-python: Python"
    ``` python
    --8<-- "user-guide/python/transformations/time-series/filter.py:negative"
    ```

```text
shape: (1, 2)
┌─────────────┬────────┐
│ ts          ┆ values │
│ ---         ┆ ---    │
│ date        ┆ i64    │
╞═════════════╪════════╡
│ -1400-03-02 ┆ 4      │
└─────────────┴────────┘
```