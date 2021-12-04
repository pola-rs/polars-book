from .dataset import df
import polars as pl

df = df.select(
    [
        pl.sum("nrs"),
        pl.col("names").sort(),
    ]
)
