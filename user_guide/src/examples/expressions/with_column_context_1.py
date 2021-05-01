from .dataset import df
import polars as pl
from polars import col

df = df.with_columns(
    [pl.sum("nrs").alias("nrs_sum"), col("random").count().alias("count")]
)
