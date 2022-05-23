import polars as pl

df = pl.read_csv("data/appleStock.csv", parse_dates=True)

filtered_df = df.filter(pl.col("Date") == pl.datetime(1995, 10, 16))

filtered_range_df = df.filter(pl.col("Date").is_between(pl.datetime(1995, 7, 1), pl.datetime(1995, 11, 1)))

annual_average_df = df.groupby_dynamic("Date", every="1y").agg(pl.col("Close").mean())
