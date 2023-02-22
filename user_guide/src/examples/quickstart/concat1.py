from .join_df1 import df1
from .join_df2 import df2
import polars as pl

out = pl.concat([df1,df2], how="horizontal")
