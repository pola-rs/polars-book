import polars as pl

df = pl.read_csv("data/appleStock.csv", parse_dates=False)

df = df.with_column(pl.col("Date").str.strptime(pl.Date, fmt="%Y-%m-%d"))
