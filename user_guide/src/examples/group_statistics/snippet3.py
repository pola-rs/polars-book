import polars as pl

from .dataset import parsed_sorted as dataset


# creates a new polars.Series with differences per row
def mkdiff(cumcases: pl.Series) -> pl.Series:
    return cumcases - cumcases.shift(1)


q = dataset.with_columns(
    [
        pl.col("cumcases")
        .apply(mkdiff)
        .over(pl.col("country"))
        .take(pl.col("country").arg_unique())
        .explode()
        .alias("diffcases"),
        pl.sum("cumcases").over("country").alias("cases/country"),
        pl.sum("cumcases").over("date").alias("sum_cases/day"),
        pl.min("cumcases").over("date").alias("min_cases/day"),
        pl.max("cumcases").over("date").alias("max_cases/day"),
        pl.sum("cumcases").over(pl.col("date").dt.year()).alias("cases/year"),
    ]
)

df = q.collect()
