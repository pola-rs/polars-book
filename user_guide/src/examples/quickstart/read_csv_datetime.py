import polars as pl

df_csv_with_dates = pl.read_csv("output.csv", try_parse_dates=True)
