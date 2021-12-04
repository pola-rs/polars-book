import polars as pl

df = pl.DataFrame({"a": [1, 2, 3], "b": [0, 1, 2]})

out = df.filter(
    pl.fold(
        acc=pl.lit(True),
        f=lambda acc, x: acc & x,
        exprs=pl.col("*") > 1,
    )
)
