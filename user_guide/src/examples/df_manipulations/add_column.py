from .dataset import df
import polars as pl

df.with_column(pl.Series(["p", "q", "r", "s", "t"]).alias("e"))
