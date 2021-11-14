from .dataset import df
import polars as pl

q = df.lazy().sort(pl.col("a"), reverse=True)
df = q.collect()
