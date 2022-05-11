import polars as pl

from .dataset import df

out = df.select([pl.sum("nrs"), pl.col("names").sort(),])
