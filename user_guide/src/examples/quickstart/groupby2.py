from .dataframe3 import df
import polars as pl

out = df.groupby("y", maintain_order=True).agg([pl.col("*").count().alias("count"), pl.col("*").sum().alias("sum")])
