import pypolars as pl
from pypolars.lazy import *
import time

reddit = pl.scan_csv("data/reddit.csv")

# doesn't really matter due to predicate optimizations
optimal = True

# reddit = reddit.filter(
#     (col("comment_karma") > 0) &
#     (col("link_karma") > 0) &
#     (col("name").str_contains(r"^a"))
# )
reddit = (
    reddit.filter(col("comment_karma") > 0)
    .filter(col("link_karma") > 0)
    .filter(col("name").str_contains(r"^a"))  # filter name that start with an "a"
)

# if optimal:
# this is exactly the same result as below as the query optimizer will combine predicates.
#     reddit = reddit.filter(
#         (col("comment_karma") > 0) &
#         (col("link_karma") > 0) &
#         (col("name").str_contains(r"^a"))
# )
# else:
#     reddit = (
#         reddit
#         .filter(col("comment_karma") > 0)
#         .filter(col("link_karma") > 0)
#         .filter(col("name").str_contains(r"^a"))  # filter name that start with an "a"
#     )

t0 = time.time()

print(reddit.show_graph(True))

# df = reddit.fetch(predicate_pushdown=True, n_rows=int(1e7))

print(time.time() - t0)
# print(df)
# print(runestar.fetch())
