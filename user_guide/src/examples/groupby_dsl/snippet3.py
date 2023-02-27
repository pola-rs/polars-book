import polars as pl

from .dataset import dataset

q = (
    dataset.lazy()
    .groupby(["state", "party"])
    .agg([pl.count("party").alias("count")])
    .filter((pl.col("party") == "Anti-Administration") | (pl.col("party") == "Pro-Administration"))
    .sort("count", descending=True)
    .limit(5)
)

df = q.collect()
