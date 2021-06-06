from .dataset import df
import polars as pl
from polars import col

df = df[[col("names").filter(col("names").str.contains(r"am$")).count()]]
