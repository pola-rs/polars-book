import polars as pl
from polars import col
from .eager_1 import df

out = df.lazy().filter(col("a") > 2).collect()
