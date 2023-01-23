# Time zones

## Parsing

You can use `'%z'` to parse timezones:

```python
{{#include ../../examples/time_series/time_zones.py:2:5}}
```

```text
{{#include ../../outputs/time_series/with_offset_parsed.txt}}
```

Note that the `'Z'` suffix for Zulu time is not yet supported - if your time string has it, you should put a `'Z'` in your format string and then cast to `'UTC'`:

```python
{{#include ../../examples/time_series/time_zones.py:7:9}}
```

```text
{{#include ../../outputs/time_series/zulu_time_parsed.txt}}
```

## Conversion

Setting time zones and converting between them can be done with `dt.with_timezone` and `dt.cast_timezone`.

Let's start with

```python
{{#include ../../examples/time_series/time_zones.py:11:11}}
```

```text
{{#include ../../outputs/time_series/tz_naive.txt}}
```

```python
{{#include ../../examples/time_series/time_zones.py:13:13}}
```

```text
{{#include ../../outputs/time_series/tz_aware.txt}}
```

and look at some examples.

### Convert tz-naive to tz-aware from UTC

```python
{{#include ../../examples/time_series/time_zones.py:15:15}}
```

```text
{{#include ../../outputs/time_series/tz_aware_from_utc.txt}}
```

### Set timezone on tz-naive

```python
{{#include ../../examples/time_series/time_zones.py:17:17}}
```

```text
{{#include ../../outputs/time_series/timezone_set_on_tz_naive.txt}}
```

### Convert tz-aware to different timezone

```python
{{#include ../../examples/time_series/time_zones.py:19:19}}
```

```text
{{#include ../../outputs/time_series/tz_aware_to_different_timezone.txt}}
```

### Change timezone of tz-aware (without conversion)

```python
{{#include ../../examples/time_series/time_zones.py:21:21}}
```

```text
{{#include ../../outputs/time_series/tz_aware_with_changed_timezone.txt}}
```

### Remove timezone from tz-aware

```python
{{#include ../../examples/time_series/time_zones.py:23:23}}
```

```text
{{#include ../../outputs/time_series/tz_aware_to_naive.txt}}
```
