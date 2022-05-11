import polars as pl

from .dataset import df

out = df.with_column(pl.Series(["p", "q", "r", "s", "t"]).alias("e"))
