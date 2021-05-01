from .dataset import df
import polars as pl
from polars import col

df = df.lazy().select([pl.sum("nrs"), col("names").sort()]).collect()
