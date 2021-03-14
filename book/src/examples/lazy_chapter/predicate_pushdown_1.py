import polars as pl
from polars.lazy import *

reddit = pl.scan_csv("data/reddit.csv")

reddit_2 = reddit.filter(
    (col("comment_karma") > 0)
    & (col("link_karma") > 0)
    & (col("name").str_contains(r"^a"))
)

if __name__ == "__main__":
    reddit_2.show_graph(
        optimized=False, show=False, output_path="book/src/img/predicate_pushdown_1.png"
    )
