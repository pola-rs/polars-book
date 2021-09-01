import polars as pl
from polars import col, lit
from .window_1 import df

out = df.sort("Type 1").select(
    [
        col("Type 1").head(3).over("Type 1").flatten(),
        col("Name").sort_by(col("Speed")).head(3).over("Type 1").flatten().alias("fastest/group"),
        col("Name").sort_by(col("Attack")).head(3).over("Type 1").flatten().alias("strongest/group"),
        col("Name").sort().head(3).over("Type 1").flatten().alias("sorted_by_alphabet"),
    ]
)
