from .dataset import df
import polars as pl

df = df[
    [
        pl.col("names").n_unique().alias("unique_names_1"),
        pl.col("names").unique().count().alias("unique_names_2"),
    ]
]
