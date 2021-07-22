import polars as pl
from polars import col, lit

df = pl.DataFrame({"a": [1, 2, 3], "b": [10, 20, 30]})

out = df.select(
    pl.fold(acc=lit(0), f=lambda acc, x: acc + x, exprs=col("*")).alias("sum")
)
