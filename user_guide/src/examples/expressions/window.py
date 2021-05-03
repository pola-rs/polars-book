from .dataset import df
import polars as pl
from polars import col

df = df[
    [
        col("*"),  # select all
        col("random").sum().over("groups").alias("sum[random]/groups"),
        col("random").list().over("names").alias("random/name"),
    ]
]
