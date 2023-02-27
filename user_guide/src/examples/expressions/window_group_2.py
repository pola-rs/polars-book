import polars as pl
from .window_group_1 import filtered

out = filtered.with_columns(
    [
        pl.col(["Name", "Speed"]).sort(descending=True).over("Type 1"),
    ]
)
