from .dataframe2 import df
import polars as pl

out = df.with_columns([(pl.col("a") * pl.col("b")).alias("a * b")]).select([pl.all().exclude("d")])
