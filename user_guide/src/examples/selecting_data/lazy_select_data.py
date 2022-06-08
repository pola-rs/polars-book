import polars as pl

lazy_select_df = pl.scan_csv("data/titanic.csv").select(["Survived", "Sex"])

lazy_select_df = lazy_select_df.describe_optimized_plan()


lazy_filter_df = pl.scan_csv("data/titanic.csv").filter(pl.col("Survived") == 1).filter(pl.col("Sex") == "female")

lazy_filter_df = lazy_filter_df.describe_optimized_plan()
