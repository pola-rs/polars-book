import polars as pl
from polars.lazy import *

# A scan is a lazy read. This means nothing happens.
reddit = pl.scan_csv("data/reddit.csv")

reddit = (
    reddit.filter(col("comment_karma") > 0)  # only positive comment karma
    .filter(col("link_karma") > 0)  # only positive link karma
    .filter(col("name").str_contains(r"^a"))  # filter name that start with an "a"
)

if __name__ == "__main__":
    df = reddit.fetch(int(1e7))
    with open("book/src/outputs/predicate_pushdown_0.txt", "w") as f:
        f.write(str(df))

    reddit.show_graph(
        optimized=False, show=False, output_path="book/src/img/predicate_pushdown_0.png"
    )
    reddit.show_graph(
        optimized=True,
        show=False,
        output_path="book/src/img/predicate_pushdown_0_optimized.png",
    )
