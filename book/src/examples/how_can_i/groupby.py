import polars as pl
from polars.lazy import col

reddit = (
    pl.scan_csv("data/reddit.csv")
    .groupby("comment_karma")
    .agg([col("name").n_unique().alias("unique_names"), pl.max("link_karma")])
    .sort(by_column="unique_names", reverse=True)
)

if __name__ == "__main__":
    df = reddit.fetch()
    with open("book/src/outputs/how_can_i_groupby.txt", "w") as f:
        f.write(str(df))
