from polars import col

from .dataset import df

q = df.lazy().sort(col("a"), reverse=True)
df = q.collect()
