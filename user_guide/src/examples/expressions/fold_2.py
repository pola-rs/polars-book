import polars as pl
from polars import col, lit

df = pl.DataFrame({"a": [1, 2, 3], "b": [0, 1, 2]})

out = df.filter(pl.fold(acc=lit(True), f=lambda acc, x: acc & x, exprs=col("*") > 1))
