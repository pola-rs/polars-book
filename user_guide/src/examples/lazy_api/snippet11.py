import polars as pl

from ..paths import DATA_DIR

q11 = (
    pl.scan_csv(f"{DATA_DIR}/reddit.csv")
    .with_columns(pl.col("name").str.to_uppercase())
    .filter(pl.col("comment_karma") > 0)
    .sink_parquet(f"{DATA_DIR}/reddit.parquet")
)
