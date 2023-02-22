import polars as pl

df_csv_with_dates = pl.read_csv('output.csv', parse_dates=True)