import polars as pl

pl.Config.set_tbl_rows(6)
pl.Config.set_tbl_cols(9)

pl.Config.set_fmt_str_lengths(30)

csv_url = "https://raw.githubusercontent.com/pola-rs/polars-static/master/data/titanic.csv"

df = pl.read_csv(csv_url)

select_df = df.select(
    [
        pl.col("Pclass"),
        pl.col("Name"),
        pl.col("Age"),
    ]
)
