import polars as pl
from .dataset import df

out = df.sort(["b", "a"], reverse=[True, False])
