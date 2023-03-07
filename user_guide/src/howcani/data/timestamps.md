# Timestamp parsing

`Polars` offers `3` absolute time datatypes

- `pl.Date`, to be used for **date** objects: the number of days since the UNIX epoch as
  a 32 bit signed integer.
- `pl.Datetime`, to be used for **datetime** objects: the number of nanoseconds since the
  UNIX epoch as a 64 bit signed integer.
- `pl.Time`, encoded as the number of nanoseconds since midnight.

`Polars` string (`pl.Utf8`) datatypes can be parsed as any of them. You can let
`Polars` try to guess the format of the date\[time\], or explicitly provide a `fmt`
rule.

For instance (check [this link](https://docs.rs/chrono/latest/chrono/format/strftime/index.html) for an comprehensive list):

- `"%Y-%m-%d"` for `"2020-12-31"`
- `"%Y/%B/%d"` for `"2020/December/31"`
- `"%B %y"` for `"December 20"`

Below a quick example:

```python
{{#include ../../examples/timestamps/snippet.py}}
```

returning:

```text
{{#include ../../outputs/timestamps/output.txt}}
```

All datetime functionality is shown in the [`dt` namespace](POLARS_PY_REF_GUIDE/series/timeseries.html).

Note that `Polars` also offers a relative time datatype: `pl.Duration` to be used for **timedelta** objects, the difference between Date, Datetime or Time as a 64 bit signed integer offering microsecond resolution. The absolute time datatypes _cannot_ be safely cast to `pl.Duration`, as they mean entirely different things. If you have a timestamp like `00:46:22` or `58H13M25S` you should write your own parser using for example [str.extract](https://pola-rs.github.io/polars/py-polars/html/reference/series/api/polars.Series.str.extract.html).
