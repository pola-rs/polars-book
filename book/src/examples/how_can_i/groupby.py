import pypolars as pl
from pypolars.lazy import *

reddit = (
    pl.scan_csv("data/reddit.csv")
    .groupby("comment_karma")
    .agg([col("name").n_unique().alias("unique_names"), col("link_karma").max()])
    .sort(by_column="unique_names", reverse=True)
)

if __name__ == "__main__":
    df = reddit.collect()
    with open("book/src/outputs/how_can_i_groupby.txt", "w") as f:
        f.write(str(df))
