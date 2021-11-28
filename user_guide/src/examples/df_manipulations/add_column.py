from .dataset import df
import polars as pl

out = df.with_column(pl.Series(["p", "q", "r", "s", "t"]).alias("e"))
