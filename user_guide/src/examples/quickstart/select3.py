from .dataframe2 import df
import polars as pl

out = df.select([
    pl.col('a'),
    pl.col('b')
]).limit(3)