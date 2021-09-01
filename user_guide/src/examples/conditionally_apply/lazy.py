import polars as pl

from .dataset import df

q = df.lazy().with_column(
    pl.when(pl.col("range") >= 5).then(pl.col("left")).otherwise(pl.col("right")).alias("foo_or_bar")
)

df = q.collect()
