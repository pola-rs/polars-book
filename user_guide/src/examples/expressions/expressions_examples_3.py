import polars as pl

from .dataset import df

out = df.select([pl.col("names").filter(pl.col("names").str.contains(r"am$")).count(),])
