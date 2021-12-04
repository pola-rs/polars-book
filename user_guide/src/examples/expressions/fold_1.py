import polars as pl

df = pl.DataFrame({"a": [1, 2, 3], "b": [10, 20, 30]})

out = df.select(
    pl.fold(acc=pl.lit(0), f=lambda acc, x: acc + x, exprs=pl.col("*")).alias("sum"),
)
