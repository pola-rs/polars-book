import polars as pl

dataset = pl.scan_csv("data/reddit.csv").select(
    [pl.sum("comment_karma"), pl.min("link_karma")]
)

df = dataset.fetch()
