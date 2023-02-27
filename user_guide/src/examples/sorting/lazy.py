from .dataset import df
import polars as pl

q = df.lazy().sort(pl.col("a"), descending=True)
df = q.collect()
