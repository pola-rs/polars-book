from .dataset import df
import polars as pl

df = df.select(
    [
        pl.sum("nrs"),
        pl.col("names").sort(),
        pl.col("names").first().alias("first name"),
        (pl.mean("nrs") * 10).alias("10xnrs"),
    ]
)
