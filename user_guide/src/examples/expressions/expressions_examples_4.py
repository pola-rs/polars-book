from .dataset import df
import polars as pl

df = df.select(
    [
        pl.when(pl.col("random") > 0.5).then(0).otherwise(pl.col("random")) * pl.sum("nrs"),
    ]
)
