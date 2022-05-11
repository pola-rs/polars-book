import polars as pl

from .dataset import df

df = df.lazy().groupby("groups").agg([pl.sum("nrs"), pl.col("random").count().alias("count"),]).collect()
