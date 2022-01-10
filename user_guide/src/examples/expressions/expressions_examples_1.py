from .dataset import df
import polars as pl

out = df.select(
    [
        pl.col("names").n_unique().alias("unique_names_1"),
        pl.col("names").unique().count().alias("unique_names_2"),
    ]
)
