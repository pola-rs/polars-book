from polars import col

from .eager import df

out = df.lazy().filter(col("a") > 2).collect()
