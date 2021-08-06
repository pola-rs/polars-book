import polars as pl

q = (
    pl.scan_csv("data/reddit.csv")
    .groupby("comment_karma")
    .agg([pl.col("name").n_unique().alias("unique_names"), pl.max("link_karma")])
    .sort(by="unique_names", reverse=True)
)

df = q.fetch()
