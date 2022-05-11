from .dynamic_ds import df
import polars as pl

out = df.groupby_dynamic(
    "time",
    every="1h",
    closed="both",
    by="groups",
    include_boundaries=True,
).agg([pl.count()])
