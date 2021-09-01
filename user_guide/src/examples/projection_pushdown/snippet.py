import polars as pl

from ..paths import DATA_DIR

reddit = (
    pl.scan_csv(f"{DATA_DIR}/reddit.csv")
    .filter(pl.col("comment_karma") > 0)
    .filter(pl.col("link_karma") > 0)
    .filter(pl.col("name").str.contains(r"^a"))
)

runescape = pl.scan_csv("data/runescape.csv", has_headers=False).select(pl.col("column_1").alias("name"))

dataset = reddit.join(runescape, on="name", how="inner").select(["name", "comment_karma", "link_karma"])

df1 = dataset.fetch(int(1e7))
df2 = dataset.fetch(int(1e7), predicate_pushdown=True, projection_pushdown=True)
