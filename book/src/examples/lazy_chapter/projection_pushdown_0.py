import polars as pl
from polars.lazy import *

reddit = pl.scan_csv("data/reddit.csv")
runescape = pl.scan_csv("data/runescape.csv", has_headers=False).select(
    col("column_1").alias("name")
)

reddit = (
    reddit.filter(col("comment_karma") > 0)
    .filter(col("link_karma") > 0)
    .filter(col("name").str_contains(r"^a"))
)

joined = reddit.join(runescape, on="name", how="inner").select(
    ["name", "comment_karma", "link_karma"]
)


if __name__ == "__main__":
    joined.show_graph(
        optimized=False,
        show=False,
        output_path="book/src/img/projection_pushdown_0.png",
    )
    joined.show_graph(
        optimized=True,
        show=False,
        output_path="book/src/img/projection_pushdown_0_optimized.png",
    )
    df = joined.fetch(int(1e7))
    with open("book/src/outputs/projection_pushdown_0.txt", "w") as f:
        f.write(str(df))
