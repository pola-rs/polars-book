import polars as pl

from .dataset import parsed_sorted as dataset


# creates a new polars.Series with differences per row
def mkdiff(cumcases: pl.Series) -> pl.Series:
    return cumcases - cumcases.shift(1)


q = dataset.with_column(
    pl.col("cumcases").apply(mkdiff).over("country").take(pl.col("country").arg_unique()).explode().alias("diffcases"),
)

df = q.collect()
