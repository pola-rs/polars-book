from .dataset import df
import polars as pl
from polars import col

df = df.select([pl.sum("nrs"), pl.col("names").sort()])
