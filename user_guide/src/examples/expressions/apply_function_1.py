import polars as pl
from .map_function_1 import df

out = df.groupby("keys", maintain_order=True).agg(
    [
        pl.col("values").apply(lambda s: s.shift()).alias("shift_map"),
        pl.col("values").shift().alias("shift_expression"),
    ]
)
