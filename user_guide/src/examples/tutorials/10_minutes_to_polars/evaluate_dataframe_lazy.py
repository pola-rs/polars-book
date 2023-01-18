import polars as pl

pl.Config.set_tbl_rows(6)
pl.Config.set_tbl_cols(9)

pl.Config.set_fmt_str_lengths(30)

csv_url = "data/titanic_mod.csv"

evaluate_grouped_df = (
    pl.scan_csv(csv_url)
    .filter(pl.col("Age") > 50)
    .groupby(["Survived", "Pclass"])
    .agg(pl.col("Id").count().alias("counts"))
    .collect()
)

fetch_grouped_df = (
    pl.scan_csv(csv_url)
    .filter(pl.col("Age") > 50)
    .groupby(["Survived", "Pclass"])
    .agg(pl.col("Id").count().alias("counts"))
    .fetch(3)
)

stream_grouped_df = (
    pl.scan_csv(csv_url)
    .filter(pl.col("Age") > 50)
    .groupby(["Survived", "Pclass"])
    .agg(pl.col("Id").count().alias("counts"))
    .collect(streaming=True)
)
