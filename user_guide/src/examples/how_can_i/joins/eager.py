import polars as pl
from .dataset import df_a, df_b

out = df_a.join(df_b, left_on=["a", "c"], right_on=["foo", "bar"], how="left")
