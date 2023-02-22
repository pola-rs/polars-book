from .dataframe2 import df
import polars as pl

out = df.sample(n=3)