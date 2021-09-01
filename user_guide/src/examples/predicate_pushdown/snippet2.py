import polars as pl

from ..paths import DATA_DIR

q = pl.scan_csv(f"{DATA_DIR}/reddit.csv").filter(
    (pl.col("comment_karma") > 0) & (pl.col("link_karma") > 0) & (pl.col("name").str.contains(r"^a"))
)

df = q.fetch(int(1e7))
