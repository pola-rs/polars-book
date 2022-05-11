import polars as pl
from .window_1 import df

out = df.select(
    [
        "Type 1",
        "Type 2",
        pl.col("Attack").mean().over("Type 1").alias("avg_attack_by_type"),
        pl.col("Defense").mean().over(["Type 1", "Type 2"]).alias("avg_defense_by_type_combination"),
        pl.col("Attack").mean().alias("avg_attack"),
    ]
)
