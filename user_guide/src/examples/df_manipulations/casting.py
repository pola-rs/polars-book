from .dataset import df
import polars as pl

out = df.with_columns(pl.col("a").cast(float))
