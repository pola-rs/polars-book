import numpy as np
import polars as pl

dataset = pl.DataFrame(
    {"range": np.arange(10), "left": ["foo"] * 10, "right": ["bar"] * 10}
)

q = dataset.lazy().with_column(
    pl.when(pl.col("range") >= 5)
    .then(pl.col("left"))
    .otherwise(pl.col("right"))
    .alias("foo_or_bar")
)

df = q.collect()
