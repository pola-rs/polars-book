import polars as pl

from .dataset import parsed_sorted as dataset


# creates a new polars.Series with differences per row
def mkdiff(cumcases: pl.Series) -> pl.Series:
    return cumcases - cumcases.shift(1)


# group by uid and aggregate to different Series lists that we later explode and join
# back on the main DataFrame
# the mkdiff function gets sorted values on date per group
q = (
    dataset.groupby("country")
    .agg(
        [
            pl.col("date").list().alias("date"),
            pl.col("cumcases").apply(mkdiff).alias("diff"),
        ]
    )
    .explode(["date", "diff"])
    .join(dataset, on=["country", "date"])
)

df = q.collect()
