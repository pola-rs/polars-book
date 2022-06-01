import polars as pl
import numpy as np

df = pl.DataFrame(
    {
        "value": [1, None],
    },
)

null_count_df = df.null_count()

is_null_series = df.select(
    pl.col("value").is_null(),
)

nan_df = pl.DataFrame(
    {
        "value": [1.0, np.NaN, float("nan"), 3.0],
    },
)
