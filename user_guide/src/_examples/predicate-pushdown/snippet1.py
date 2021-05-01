import polars as pl

from ..paths import DATA_DIR

dataset = (
    pl.scan_csv(f"{DATA_DIR}/reddit.csv")
    .filter(pl.col("comment_karma") > 0)
    .filter(pl.col("link_karma") > 0)
    .filter(pl.col("name").str_contains(r"^a"))  # filter name that start with an "a"
)

df1 = dataset.fetch(int(1e7))
df2 = dataset.fetch(int(1e7), predicate_pushdown=True)
