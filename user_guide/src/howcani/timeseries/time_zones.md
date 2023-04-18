# Time zones

> You really should never, ever deal with time zones if you can help it

-- <cite>Tom Scott</cite>

The `Datetime` datatype can have a time zone associated with it.
Examples of valid time zones are:

- `None`: no time zone, also known as "time zone naive";
- `UTC`: Coordinated Universal Time;
- `Asia/Kathmandu`: time zone in "area/location" format.
  See the [list of tz database time zones](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones)
  to see what's available;
- `+01:00`: fixed offsets. May be useful when parsing, but you almost certainly want the "Area/Location"
  format above instead as it will deal with irregularities such as DST (Daylight Saving Time) for you.

Note that, because a `Datetime` can only have a single time zone, it is
impossible to have a column with multiple time zones. If you are parsing data
with multiple offsets, you may want to pass `utc=True` to convert
them all to a common time zone (`UTC`), see [parsing dates and times](parsing_dates_times.md).

The main methods for setting and converting between time zones are:

- `dt.convert_time_zone`: convert from one time zone to another;
- `dt.replace_time_zone`: set/unset/change time zone;

Let's look at some examples of common operations:

```python
{{#include ../../examples/time_series/time_zones/snippet.py:03:06}}
```

```text
{{#include ../../outputs/time_series/time_zones/time_zones_df.txt}}
```

```python
{{#include ../../examples/time_series/time_zones/snippet.py:08:14}}
```

```text
{{#include ../../outputs/time_series/time_zones/time_zones_operations.txt}}
```
