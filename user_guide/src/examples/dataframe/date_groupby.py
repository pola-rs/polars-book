import polars as pl
from .datatypes import df


res = (
    df.groupby(
        [
            pl.col("date").dt.year().alias("year"),
            pl.col("date").dt.month().alias("month"),
            pl.col("color"),
        ]
    )
    .agg([pl.col("rank").alias("best_of_month").min()])
    .sort([pl.col("best_of_month")])
)
