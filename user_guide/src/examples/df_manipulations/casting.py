from .dataset import df
import polars as pl

out = df.with_column(pl.col("a").cast(float))
