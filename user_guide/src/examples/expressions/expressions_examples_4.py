import polars as pl

from .dataset import df

out = df.select([pl.when(pl.col("random") > 0.5).then(0).otherwise(pl.col("random")) * pl.sum("nrs"),])
