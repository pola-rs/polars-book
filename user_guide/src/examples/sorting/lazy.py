import polars as pl

from .dataset import df

q = df.lazy().sort(pl.col("a"), reverse=True)
df = q.collect()
