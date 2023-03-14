from .dataset import df
import polars as pl

out = df.select(
    [
        pl.when(pl.col("groups") == "A").then(1)
        .when(pl.col("random") > 0.5).then(0)
        .otherwise(pl.col("random"))
    ]
)
