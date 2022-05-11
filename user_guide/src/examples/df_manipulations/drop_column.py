import polars as pl

from .dataset import df

# drop single column
out = df.drop("d")

# drop multiple columns
out = df.drop(["b", "c"])

# select all but "b" and "c"
out = df.select(pl.all().exclude(["b", "c"]))

# select only "a"
out = df.select(pl.col("a"))
