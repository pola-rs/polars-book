import polars as pl
from .map_function_1 import df

out = df.select(
    [
        pl.struct(["keys", "values"]).apply(lambda x: len(x["keys"]) + x["values"]).alias("solution_apply"),
        (pl.col("keys").str.lengths() + pl.col("values")).alias("solution_expr"),
    ]
)
