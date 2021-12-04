from .dataset import df
import polars as pl

df = df.groupby("groups").agg(
    [
        pl.sum("nrs"),
        pl.col("random").count().alias("count"),
    ]
)
