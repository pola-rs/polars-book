import polars as pl

from ..paths import DATA_DIR

q1 = (
    pl.scan_csv(f"{DATA_DIR}/reddit.csv")
    .with_columns(pl.col("name").str.to_uppercase())
    .filter(pl.col("comment_karma") > 0)
)

q1.describe_plan()

q1_plan = q1.describe_plan()

q1.describe_optimized_plan()

q1_opt_plan = q1.describe_optimized_plan()

q1.show_graph(optimized=False)

q1.show_graph()
