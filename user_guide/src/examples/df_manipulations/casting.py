import polars as pl

from .dataset import df

out = df.with_column(pl.col("a").cast(float))
