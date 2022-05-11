import polars as pl

from .dataset import df

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
