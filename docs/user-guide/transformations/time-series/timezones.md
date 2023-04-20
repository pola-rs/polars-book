---
hide:
  - toc
---
# Time zones

!!! quote "Tom Scott"
    You really should never, ever deal with time zones if you can help it

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
them all to a common time zone (`UTC`), see [parsing dates and times](parsing.md).

The main methods for setting and converting between time zones are:

- `dt.convert_time_zone`: convert from one time zone to another;
- `dt.replace_time_zone`: set/unset/change time zone;

Let's look at some examples of common operations:

=== ":fontawesome-brands-python: Python"
    ``` python
    --8<-- "user-guide/python/transformations/time-series/timezones.py:example"
    ```

```text
shape: (2, 2)
┌─────────────────────┬─────────────────────────┐
│ tz_naive            ┆ tz_aware                │
│ ---                 ┆ ---                     │
│ datetime[μs]        ┆ datetime[μs, UTC]       │
╞═════════════════════╪═════════════════════════╡
│ 2021-03-27 03:00:00 ┆ 2021-03-27 03:00:00 UTC │
│ 2021-03-28 03:00:00 ┆ 2021-03-28 03:00:00 UTC │
└─────────────────────┴─────────────────────────┘
```

=== ":fontawesome-brands-python: Python"
    ``` python
    --8<-- "user-guide/python/transformations/time-series/timezones.py:example2"
    ```

```text
shape: (2, 3)
┌───────────────────────────────┬──────────────────────────────┬─────────────────────┐
│ replace time zone             ┆ convert time zone            ┆ unset time zone     │
│ ---                           ┆ ---                          ┆ ---                 │
│ datetime[μs, Europe/Brussels] ┆ datetime[μs, Asia/Kathmandu] ┆ datetime[μs]        │
╞═══════════════════════════════╪══════════════════════════════╪═════════════════════╡
│ 2021-03-27 03:00:00 CET       ┆ 2021-03-27 08:45:00 +0545    ┆ 2021-03-27 03:00:00 │
│ 2021-03-28 03:00:00 CEST      ┆ 2021-03-28 08:45:00 +0545    ┆ 2021-03-28 03:00:00 │
└───────────────────────────────┴──────────────────────────────┴─────────────────────┘
```