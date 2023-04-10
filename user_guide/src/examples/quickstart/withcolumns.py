from .dataframe2 import df
import polars as pl

out = df.with_columns([pl.col("b").sum().alias("e"), (pl.col("b") + 42).alias("b+42")])
