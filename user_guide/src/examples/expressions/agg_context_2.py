from .dataset import df
import polars as pl

df = (
    df.lazy()
    .groupby("groups")
    .agg(
        [
            pl.sum("nrs"),
            pl.col("random").count().alias("count"),
        ]
    )
    .collect()
)
