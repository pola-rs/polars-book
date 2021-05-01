from .dataset import df
import polars as pl
from polars import col

df = df[[pl.when(col("random") > 0.5).then(0).otherwise(col("random")) * pl.sum("nrs")]]
