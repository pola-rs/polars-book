import numpy as np
import polars as pl
from polars.lazy import col, when

df = pl.DataFrame({"range": np.arange(10), "left": ["foo"] * 10, "right": ["bar"] * 10})

out = df.lazy().with_column(
    when(col("range") >= 5)
    .then(col("left"))
    .otherwise(col("right"))
    .alias("foo_or_bar")
)

if __name__ == "__main__":
    with open("user_guide/src/outputs/how_can_i_conditionally_apply.txt", "w") as f:
        f.write(str(out.collect()))
