# Filtering date columns

Filtering date columns works in the same way as with other types of columns using the `.filter` method.

Polars uses Python's native `datetime`, `date` and `timedelta` for equality comparisons between the datatypes
`pl.Datetime`, `pl.Date` and `pl.Duration`.

In the following example we use a time series of Apple stock prices.

```python
{{#include ../../examples/time_series/parsing_dates.py:1:4}}
print(df)
```

```text
{{#include ../../outputs/time_series/parse_dates_example_df.txt}}
```

## Filtering by single dates

We can filter by a single date by casting the desired date string to a `Date` object
in a filter expression:

```python
{{#include ../../examples/time_series/parsing_dates.py:6:8}}
```

```text
{{#include ../../outputs/time_series/parse_dates_filtered_df.txt}}
```

Note we are using the lowercase `datetime` method rather than the uppercase `Datetime` data type.

## Filtering by a date range

We can filter by a range of dates using the `is_between` method in a filter expression with the start and end dates:

```python
{{#include ../../examples/time_series/parsing_dates.py:10:12}}
```

```text
{{#include ../../outputs/time_series/parse_dates_filtered_range_df.txt}}
```

## Filtering with negative dates

Say you are working with an archeologist and are dealing in negative dates.
Polars can parse and store them just fine, but the Python `datetime` library
does not. So for filtering, you should use attributes in the `.dt` namespace:

```python
{{#include ../../examples/time_series/parsing_dates.py:18:22}}
```

```text
{{#include ../../outputs/time_series/negative_dates_filtered_df.txt}}
```
