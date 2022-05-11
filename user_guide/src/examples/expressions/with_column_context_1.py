import polars as pl

from .dataset import df

df = df.with_columns([pl.sum("nrs").alias("nrs_sum"), pl.col("random").count().alias("count"),])
