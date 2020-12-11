import pypolars as pl
from pypolars.lazy import *
import time

reddit = pl.scan_csv("data/reddit.csv")
runestar = pl.scan_csv("data/runescape.csv", has_headers=False).with_column(
    col("column_1").alias("name")
)

reddit = (
    reddit.filter(col("comment_karma") > 0)
    .filter(col("link_karma") > 0)
    .filter(col("name").str_contains(r"^a"))  # filter name that start with an "a"
)

joined = reddit.join(runestar, on="name", how="inner").select(
    ["name", "comment_karma", "link_karma"]
)

t0 = time.time()

joined.show_graph(True)

df = joined.fetch(int(1e7))

print(time.time() - t0)
print(df)
