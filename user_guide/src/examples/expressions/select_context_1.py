from .dataset import df
import polars as pl

df = df[[pl.sum("nrs"), pl.col("names").sort()]]
