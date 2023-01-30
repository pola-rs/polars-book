# Time zones

## Parsing

# See the chrono docs for which directives to use to parse timezones.

You can use `'%z'` to parse timezones:

```python
{{#include ../../examples/time_series/time_zones.py:2:5}}
```

```text
{{#include ../../outputs/time_series/with_offset_parsed.txt}}
```

## Conversion

The main methods for setting and converting between time zones are:
- ``dt.with_time_zone``: convert to a given time zone;
- ``dt.cast_time_zone``: set given time zone.

Let's start with

```python
{{#include ../../examples/time_series/time_zones.py:07:07}}
```

```text
{{#include ../../outputs/time_series/tz_naive.txt}}
```

```python
{{#include ../../examples/time_series/time_zones.py:09:09}}
```

```text
{{#include ../../outputs/time_series/tz_aware.txt}}
```

and look at some examples.

### Convert tz-naive to tz-aware from UTC

```python
{{#include ../../examples/time_series/time_zones.py:11:11}}
```

```text
{{#include ../../outputs/time_series/tz_aware_from_utc.txt}}
```

### Set timezone on tz-naive

```python
{{#include ../../examples/time_series/time_zones.py:13:13}}
```

```text
{{#include ../../outputs/time_series/timezone_set_on_tz_naive.txt}}
```

### Convert tz-aware to different timezone

```python
{{#include ../../examples/time_series/time_zones.py:14:14}}
```

```text
{{#include ../../outputs/time_series/tz_aware_to_different_timezone.txt}}
```

### Change timezone of tz-aware (without conversion)

```python
{{#include ../../examples/time_series/time_zones.py:17:17}}
```

```text
{{#include ../../outputs/time_series/tz_aware_with_changed_timezone.txt}}
```

### Remove timezone from tz-aware

```python
{{#include ../../examples/time_series/time_zones.py:19:19}}
```

```text
{{#include ../../outputs/time_series/tz_aware_to_naive.txt}}
```
