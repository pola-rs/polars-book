from .dataframe2 import df
import polars as pl
from datetime import datetime

out = df.filter(
    (pl.col('a') <= 3) & (pl.col('d').is_not_nan())
)
