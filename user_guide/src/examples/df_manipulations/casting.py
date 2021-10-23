from .dataset import df
import polars as pl

df.with_column(pl.col("a").cast(float))
