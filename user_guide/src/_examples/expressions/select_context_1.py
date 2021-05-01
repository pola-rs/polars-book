from .dataset import df
import polars as pl
from polars import col

df = df[[pl.sum("nrs"), col("names").sort()]]
