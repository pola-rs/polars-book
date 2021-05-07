import polars as pl
from polars import col

df = pl.DataFrame({"a": [1, 2, 3], "b": [None, "b", "c"]})

mask = df["a"] > 2
out = df[mask]
