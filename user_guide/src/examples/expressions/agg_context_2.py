from .dataset import df
import polars as pl
from polars import col

df = (
    df.lazy()
    .groupby("groups")
    .agg([pl.sum("nrs"), col("random").count().alias("count")])
    .collect()
)
