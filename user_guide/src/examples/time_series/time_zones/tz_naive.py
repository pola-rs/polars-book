import polars as pl

tz_naive = pl.Series(["2020-01-01 03:00:00"]).str.strptime(pl.Datetime)
