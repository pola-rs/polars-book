import polars as pl
from datetime import datetime

lazy_select_df = pl.scan_csv("data/appleStock.csv").select(["Date"])

lazy_select_df = lazy_select_df.describe_optimized_plan()

lazy_filter_df = (
    pl.scan_csv("data/appleStock.csv")
    .filter(
        pl.col("Date") == datetime(1995, 10, 16),
    )
    .filter(pl.col("Close") > 100)
)

lazy_filter_df = lazy_filter_df.describe_optimized_plan()
