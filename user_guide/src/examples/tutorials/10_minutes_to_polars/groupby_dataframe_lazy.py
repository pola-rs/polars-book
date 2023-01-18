import polars as pl

pl.Config.set_tbl_rows(6)
pl.Config.set_tbl_cols(9)

pl.Config.set_fmt_str_lengths(30)

csv_url = "data/titanic_mod.csv"

lazy_grouped_df = (
    pl.scan_csv(csv_url)
    .groupby(["Survived", "Pclass"])
    .agg([pl.col("Id").count().alias("counts"), pl.col("Age").mean().alias("average_age")])
)

lazy_grouped_plan = lazy_grouped_df.describe_optimized_plan()
