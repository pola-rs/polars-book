# Timestamp parsing

`Polars` offers two time datatypes:

- `pl.Date32`, to be used for **date** objects: the number of days since the UNIX epoch as
  a 32 bit signed integer.
- `pl.Date64`, to be used of **datetime** ojects: the number of milliseconds since the
  UNIX epoch as a 64 bit signed integer.

`Polars` string (`pl.Utf8`) datatypes can be parsed as either of them. One can let
`Polars` try to guess the format of the date\[time\], or explicitly provide a `fmt`
rule.

For instance (check [this link](https://strftime.org/) for an comprehensive list):

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

All datetime functionality is shown in the [`dt` namespace](POLARS_PY_REF_GUIDE/series.html#timeseries).
