import polars as pl
from datetime import datetime

df = pl.read_csv("data/appleStock.csv", parse_dates=True)

filtered_df = df.filter(
    pl.col("Date") == datetime(1995, 10, 16),
)

filtered_range_df = df.filter(
    pl.col("Date").is_between(datetime(1995, 7, 1), datetime(1995, 11, 1)),
)

annual_average_df = df.groupby_dynamic("Date", every="1y").agg(pl.col("Close").mean())

df_with_year = df.with_column(pl.col("Date").dt.year().alias("year"))

ts = pl.Series(["-1300-05-23", "-1400-03-02"]).str.strptime(pl.Date)

negative_dates_df = pl.DataFrame({"ts": ts, "values": [3, 4]})

negative_dates_filtered_df = negative_dates_df.filter(pl.col("ts").dt.year() < -1300)
