import polars as pl
from .window_1 import df

out = df.sort("Type 1").select(
    [
        pl.col("Type 1").head(3).over("Type 1").flatten(),
        pl.col("Name").sort_by(pl.col("Speed")).head(3).over("Type 1").flatten().alias("fastest/group"),
        pl.col("Name").sort_by(pl.col("Attack")).head(3).over("Type 1").flatten().alias("strongest/group"),
        pl.col("Name").sort().head(3).over("Type 1").flatten().alias("sorted_by_alphabet"),
    ]
)
