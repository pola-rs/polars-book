import polars as pl

df = pl.DataFrame({"a": [1, 2, 3], "b": [None, "b", "c"]})

out = df.lazy().filter(pl.col("a") > 2).collect()
