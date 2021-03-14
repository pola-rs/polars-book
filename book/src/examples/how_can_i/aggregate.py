import polars as pl
from polars.lazy import *

reddit = pl.scan_csv("data/reddit.csv").select(
    [pl.sum("comment_karma"), pl.min("link_karma")]
)

if __name__ == "__main__":
    df = reddit.fetch()
    with open("book/src/outputs/how_can_i_aggregate.txt", "w") as f:
        f.write(str(df))
