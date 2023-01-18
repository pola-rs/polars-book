import polars as pl

pl.Config.set_tbl_rows(6)
pl.Config.set_tbl_cols(9)

pl.Config.set_fmt_str_lengths(30)

csv_url = "https://raw.githubusercontent.com/pola-rs/polars-static/master/data/titanic.csv"

df = pl.read_csv(csv_url)

grouped_df = df.groupby(["Survived", "Pclass"]).agg(
    [pl.col("Id").count().alias("counts"), pl.col("Age").mean().alias("average_age")]
)
