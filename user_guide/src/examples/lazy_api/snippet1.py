import polars as pl

from ..paths import DATA_DIR

q1 = (
    pl.scan_csv(f"{DATA_DIR}/reddit.csv")
    .filter(pl.col("comment_karma") > 0)
    .filter(pl.col("link_karma") > 0)
    .filter(pl.col("name").str.contains(r"^a"))  # filter name that start with an "a"
)

q1.describe_plan()

q1_plan = q1.describe_plan()

q1.describe_optimized_plan()

q1_opt_plan = q1.describe_optimized_plan()
