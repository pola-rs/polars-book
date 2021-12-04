from .dataset import df
import polars as pl

df = (
    df.lazy()
    .with_columns(
        [
            pl.sum("nrs").alias("nrs_sum"),
            pl.col("random").count().alias("count"),
        ]
    )
    .collect()
)
