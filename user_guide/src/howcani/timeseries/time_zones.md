# Time zones

> You really should never, ever deal with time zones if you can help it

-- <cite>Tom Scott</cite>

The main methods for setting and converting between time zones are:

- `dt.convert_time_zone`: convert from one time zone to another;
- `dt.replace_time_zone`: set/unset/change time zone;

Let's look at some examples of common operations:

```python
{{#include ../../examples/time_series/time_zones.py:03:06}}
```

```text
{{#include ../../outputs/time_series/time_zones/time_zones_df.txt}}
```

```python
{{#include ../../examples/time_series/time_zones.py:08:14}}
```

```text
{{#include ../../outputs/time_series/time_zones/time_zones_operations.txt}}
```

See the [list of tz database time zones](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones)
for a list of what's available.
