import polars as pl

df = pl.read_csv("data/appleStock.csv", try_parse_dates=False)

df = df.with_columns(pl.col("Date").str.strptime(pl.Date, fmt="%Y-%m-%d"))
