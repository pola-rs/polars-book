import numpy as np
import polars as pl

src_df = pl.DataFrame(
    {"range": np.arange(10), "left": ["foo"] * 10, "right": ["bar"] * 10}
)

dataset = src_df.lazy().with_column(
    pl.when(pl.col("range") >= 5)
    .then(pl.col("left"))
    .otherwise(pl.col("right"))
    .alias("foo_or_bar")
)

df = dataset.collect()
