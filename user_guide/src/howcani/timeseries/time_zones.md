# Time zones

> You really should never, ever deal with time zones if you can help it

-- <cite>Tom Scott</cite>

The main methods for setting and converting between time zones are:

- `dt.with_time_zone`: convert from one time zone to another;
- `dt.cast_time_zone`: set/unset/change time zone.

Let's look at some examples:

```python
{{#include ../../examples/time_series/time_zones/tz_naive.py:03:03}}
```

```text
{{#include ../../outputs/time_series/time_zones/tz_naive.txt}}
```

```python
{{#include ../../examples/time_series/time_zones/tz_aware.py:03:03}}
```

```text
{{#include ../../outputs/time_series/time_zones/tz_aware.txt}}
```

```python
{{#include ../../examples/time_series/time_zones/set_time_zone.py:03:03}}
```

```text
{{#include ../../outputs/time_series/time_zones/set_time_zone.txt}}
```

```python
{{#include ../../examples/time_series/time_zones/change_time_zone.py:03:03}}
```

```text
{{#include ../../outputs/time_series/time_zones/change_time_zone.txt}}
```

```python
{{#include ../../examples/time_series/time_zones/convert_time_zone.py:03:03}}
```

```text
{{#include ../../outputs/time_series/time_zones/convert_time_zone.txt}}
```

```python
{{#include ../../examples/time_series/time_zones/unset_time_zone.py:03:03}}
```

```text
{{#include ../../outputs/time_series/time_zones/unset_time_zone.txt}}
```

See the [list of tz database time zones](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones)
for a list of what's available.
