# Date parsing

Polars has two date data types:

* Date32 
    - a naive date represented as the number of days since the unix epoch as a 32 bit signed integer.
    - Use this for Date objects
* Date64
    - a naive datetime represented as the number of milliseconds since the unix epoch as a 64 bit signed integer.
    - Use this for DateTime objects

Utf8 types can be parsed as one of the two date datetypes. You can try to let Polars parse the date(time) implicitly or
apply you `fmt` rule. Some examples are:

* `"%Y-%m-%d"` for `"2020-12-31"`
* `"%Y/%B/%d"` for `"2020/December/31"`
* `"%B %y"` for `"December 20"`

## Examples

```python
{{#include ../examples/how_can_i/parse_dates.py:4:10}}
print(parsed.collect())
```

```text
{{#include ../outputs/how_can_i_parse_dates_1.txt}}
```
