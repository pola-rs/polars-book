import polars as pl
from .map_function_1 import df

counter = 0


def add_counter(val: int) -> int:
    global counter
    counter += 1
    return counter + val


out = df.select(
    [
        pl.col("values").apply(add_counter).alias("solution_apply"),
        (pl.col("values") + pl.arange(1, pl.count() + 1)).alias("solution_expr"),
    ]
)
