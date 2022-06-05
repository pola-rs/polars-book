import polars as pl
from .add_col import df

df = df.with_column(
    pl.when(
        pl.col("rank") > 50,
    )
    .then(
        pl.lit("red"),
    )
    .otherwise(
        pl.col("color"),
    )
    .alias("color")
)
