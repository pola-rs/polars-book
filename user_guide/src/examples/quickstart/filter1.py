from .dataframe2 import df
import polars as pl
from datetime import datetime

out = df.filter(
    pl.col("c").is_between(datetime(2022, 12, 2), datetime(2022, 12, 8)),
)
