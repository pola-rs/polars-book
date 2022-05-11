import polars as pl

from .dataset import df

out = df.select(
    [pl.col("names").n_unique().alias("unique_names_1"), pl.col("names").unique().count().alias("unique_names_2"),]
)
