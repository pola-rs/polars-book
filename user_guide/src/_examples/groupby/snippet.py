import polars as pl

dataset = (
    pl.scan_csv("data/reddit.csv")
    .groupby("comment_karma")
    .agg([pl.col("name").n_unique().alias("unique_names"), pl.max("link_karma")])
    .sort(by_column="unique_names", reverse=True)
)

df = dataset.fetch()
