from .dataset import df
import polars as pl

df = df[[pl.col("names").filter(pl.col("names").str.contains(r"am$")).count()]]
