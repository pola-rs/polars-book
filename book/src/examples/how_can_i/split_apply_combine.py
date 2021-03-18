import polars as pl
from polars.lazy import col, lit
import numpy as np

uid = [item for sublist in [4 * [r] for r in range(3)] for item in sublist]
date = [
    "2020-12-20",
    "2020-12-21",
    "2020-12-22",
    "2020-12-23",
]
cumcases = [20, 40, 67, 80]

df = pl.DataFrame(
    {
        "uid": uid,
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
    # next create a sorting key defined by the group uid + date_integer
    .with_column(
        (col("uid").cast(str) + lit("-") + col("date").cast(int)).alias("sort_key")
    )
    # sort all values on the sorting key so that
    # the mkdiff function get's sorted values on date per group
    .sort("sort_key")
)

# Next we group by uid and aggregate to different
# Series lists that we later explode and join back on the main DataFrame
out = (
    base_df.groupby("uid")
    .agg(
        [
            col("date").list().alias("date"),
            col("cumcases").apply(mkdiff).alias("diff_cases"),
        ]
    )
    .explode(["date", "diff_cases"])
    .join(base_df, on=["uid", "date"])
)

if __name__ == "__main__":
    with open("book/src/outputs/how_can_i_split_apply_combine_1.txt", "w") as f:
        f.write(str(df))
    with open("book/src/outputs/how_can_i_split_apply_combine_2.txt", "w") as f:
        f.write(str(out.collect()))
