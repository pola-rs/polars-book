# Parsing dates and times

## Datatypes

`Polars` has the following datetime datatypes:

- `Date`: Date representation e.g. 2014-07-08. It is internally represented as days since UNIX epoch encoded by a 32-bit signed integer.
- `Datetime`: Datetime representation e.g. 2014-07-08 07:00:00. It is internally represented as a 64 bit integer since the Unix epoch and can have different units such as ns, us, ms.
- `Duration`: A time delta type that is created when subtracting `Date/Datetime`. Similar to `timedelta` in python.
- `Time`: Time representation, internally represented as nanoseconds since midnight.

## Parsing dates from a file

When loading from a CSV file `Polars` attempts to parse dates and times if the `try_parse_dates` flag is set to `True`:

```python
{{#include ../../examples/time_series/parsing_dates.py:4:4}}
print(df)
```

```text
{{#include ../../outputs/time_series/parse_dates_example_df.txt}}
```

On the other hand binary formats such as parquet have a schema that is respected by `Polars`.

## Casting strings to dates

You can also cast a column of datetimes encoded as strings to a datetime type. You do this by calling the string `str.strptime` method and passing the format of the date string:

```python
{{#include ../../examples/time_series/cast_date_to_string.py:3:}}
print(df)
```

```text
{{#include ../../outputs/time_series/cast_string_to_date_example_df.txt}}
```

[The strptime date formats can be found here.](https://docs.rs/chrono/latest/chrono/format/strftime/index.html).

## Extracting date features from a date column

You can extract data features such as the year or day from a date column using the `.dt` namespace on a date column:

```python
{{#include ../../examples/time_series/parsing_dates.py:16:16}}
print(df_with_year)
```

```text
{{#include ../../outputs/time_series/parse_dates_with_year.txt}}
```

See the [API docs](POLARS_PY_REF_GUIDE/series/timeseries.html)
for more date feature options.

## Mixed offsets

If you have mixed offsets (say, due to crossing daylight saving time),
then you can use `utc=True` and then convert to your time zone:

```python
{{#include ../../examples/time_series/time_zones/mixed_offsets.py:03:09}}
```

```text
{{#include ../../outputs/time_series/time_zones/mixed_parsed.txt}}
```
