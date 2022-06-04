import polars as pl
from .replace import df


df = df.with_columns(
    [
        pl.col("rank").cast(pl.Int16).alias("rank"),
        pl.col("color").cast(pl.Categorical).alias("color"),
        pl.col("id").str.extract(r"0(\w+)", 1).cast(pl.Int16).alias("id"),
    ]
)
