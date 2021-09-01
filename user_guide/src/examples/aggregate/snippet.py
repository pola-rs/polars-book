import polars as pl

q = pl.scan_csv("data/reddit.csv").select([pl.sum("comment_karma"), pl.min("link_karma")])

df = q.fetch()
