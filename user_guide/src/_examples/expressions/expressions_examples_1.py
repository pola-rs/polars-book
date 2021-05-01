from .dataset import df
import polars as pl
from polars import col

df = df[
    [
        col("names").n_unique().alias("unique_names_1"),
        col("names").unique().count().alias("unique_names_2"),
    ]
]
