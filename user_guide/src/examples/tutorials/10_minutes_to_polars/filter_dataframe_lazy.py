import polars as pl

pl.Config.set_tbl_rows(6)
pl.Config.set_tbl_cols(9)

pl.Config.set_fmt_str_lengths(30)

csv_url = "data/titanic_mod.csv"

lazy_filter_grouped_df = (
    pl.scan_csv(csv_url)
    # Add a filter for passengers over 50
    .filter(pl.col("Age") > 50)
    .groupby(["Survived", "Pclass"])
    .agg(pl.col("Id").count().alias("counts"))
    .describe_optimized_plan()
)
