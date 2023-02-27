import polars as pl

from .dataset import dataset

q = (
    dataset.lazy()
    .groupby("first_name")
    .agg(
        [
            pl.count(),
            pl.col("gender"),
            pl.first("last_name"),
        ]
    )
    .sort("count", descending=True)
    .limit(5)
)

df = q.collect()
