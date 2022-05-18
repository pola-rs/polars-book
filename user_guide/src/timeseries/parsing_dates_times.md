# Parsing dates and times

## Datatypes

`Polars` inherits the following datetime datatypes from Apache Arrow:

- `Date`: Date representation (e.g. 2014-07-08), internally represented as days since UNIX epoch encoded by a 32-bit signed integer.
- `Datetime`: Datetime representation (e.g. ), internally represented as nanoseconds since UNIX
  epoch encoded by a 64-bit signed integer.
- `Duration`: A timedelate type. Created when subtracting `Date/Datetime`.
- `Time`: Time representation, internally represented as nanoseconds since midnight.

## Parsing dates from a file

When loading from a file `Polars` attempts to parse dates and times if the `parse_dates` flag is set to `True`.

```python
{{#include ../examples/time_series/parsing_dates.py:3:3}}
print(df)
```

```text
{{#include ../outputs/time_series/parse_dates_example_df.txt}}
```

## Casting strings to dates

You can also cast a column of datetimes encoded as strings to a datetime type. You do this by calling the string `str.strptime` method and passing the format of the date string:

```python
{{#include ../examples/time_series/cast_date_to_string.py:3:}}
print(df)
```

```text
{{#include ../outputs/time_series/cast_string_to_date_example_df.txt}}
```

[The strptime date formats can be found here.](https://docs.rs/chrono/latest/chrono/format/strftime/index.html).
