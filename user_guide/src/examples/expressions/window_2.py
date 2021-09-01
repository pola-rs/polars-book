import polars as pl
from polars import col, lit
from .window_1 import df

out = df.select(
    [
        "Type 1",
        "Type 2",
        col("Attack").mean().over("Type 1").alias("avg_attack_by_type"),
        col("Defense").mean().over(["Type 1", "Type 2"]).alias("avg_attack_by_type_combination"),
        col("Attack").mean().alias("avg_attack"),
    ]
)
