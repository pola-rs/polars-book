import polars as pl

from .dataset import dataset

q = (
    dataset.lazy()
    .groupby("first_name")
    .agg(
        [
            pl.count(),
            pl.col("gender").list(),
            pl.first("last_name"),
        ]
    )
    .sort("count", reverse=True)
    .limit(5)
)

df = q.collect()
