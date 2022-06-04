import polars as pl
from .dataset import df

df = df.with_column(pl.lit("blue").alias("color"))
