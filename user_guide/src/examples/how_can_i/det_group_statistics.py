import polars as pl
from polars.lazy import col, lit
import numpy as np

country = [
    item
    for sublist in [4 * [r] for r in ["belgium", "united-kingdom", "china"]]
    for item in sublist
]
date = [
    "2020-12-20",
    "2020-12-21",
    "2020-12-22",
    "2020-12-23",
]
cumcases = [20, 40, 67, 80]

df = pl.DataFrame(
    {
        "country": country,
        "date": np.hstack([date, date, date]),
        "cumcases": np.hstack(
            [cumcases, [2 * c for c in cumcases], [3 * c for c in cumcases]]
        ),
    }
)


def mkdiff(cumcases: pl.Series) -> pl.Series:
    """
    Creates a new Series with differences per row
    """
    return cumcases - cumcases.shift(1)


base_df = (
    df.lazy()
    # first parse column as date32
    .with_column(col("date").str_parse_date(pl.Date32))
    # next create a sorting key defined by the group country + date_integer
    .with_column(
        (col("country").cast(str) + lit("-") + col("date").cast(int)).alias("sort_key")
    )
    # sort all values on the sorting key so that
    # the mkdiff function get's sorted values on date per group
    .sort("sort_key")
)

# Next we group by country and aggregate to different
# Series lists that we later explode and join back on the main DataFrame
out = (
    base_df.groupby("country")
    .agg(
        [
            col("date").list().alias("date"),
            col("cumcases").apply(mkdiff).alias("diff_cases"),
        ]
    )
    .explode(["date", "diff_cases"])
    .join(base_df, on=["country", "date"])
)

out1 = base_df.with_column(
    col("cumcases")
    .apply(mkdiff)
    .over("country")
    .take(col("country").arg_unique())
    .explode()
    .alias("diffcases"),
)

out2 = base_df.with_columns(
    [
        col("cumcases")
        .apply(mkdiff)
        .over(col("country"))
        .take(col("country").arg_unique())
        .explode()
        .alias("diffcases"),
        pl.sum("cumcases").over("country").alias("cases/country"),
        pl.sum("cumcases").over("date").alias("sum_cases/day"),
        pl.min("cumcases").over("date").alias("min_cases/day"),
        pl.max("cumcases").over("date").alias("max_cases/day"),
        pl.sum("cumcases").over(col("date").year()).alias("cases/year"),
    ]
)

if __name__ == "__main__":
    with open("user_guide/src/outputs/det_group_statistics_1.txt", "w") as f:
        f.write(str(df))
    with open("user_guide/src/outputs/det_group_statistics_2.txt", "w") as f:
        f.write(str(out.collect()))
    with open("user_guide/src/outputs/det_group_statistics_3.txt", "w") as f:
        f.write(str(out1.collect()))
    with open("user_guide/src/outputs/det_group_statistics_4.txt", "w") as f:
        f.write(str(out2.collect()))
