from .dataset import df
import polars as pl

df = df[
    [
        pl.sum("random").alias("sum"),
        pl.min("random").alias("min"),
        pl.max("random").alias("max"),
        pl.col("random").max().alias("other_max"),
        pl.std("random").alias("std dev"),
        pl.var("random").alias("variance"),
    ]
]
