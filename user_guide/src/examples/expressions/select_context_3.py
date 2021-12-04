from .dataset import df
import polars as pl

df = (
    df.lazy()
    .select(
        [
            pl.sum("nrs"),
            pl.col("names").sort(),
        ]
    )
    .collect()
)
