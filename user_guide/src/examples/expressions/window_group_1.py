import polars as pl
from .window_1 import df

filtered = df.filter(pl.col("Type 2") == "Psychic").select(
    [
        "Name",
        "Type 1",
        "Speed",
    ]
)
