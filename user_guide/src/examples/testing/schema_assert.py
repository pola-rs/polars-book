import polars as pl
import os

os.chdir("user_guide")

trip_duration = (pl.col("dropoff_datetime") - pl.col("pickup_datetime")).dt.seconds() / 3600

assert (
    pl.scan_csv("data/yellow_tripdata_2010-01.csv", parse_dates=True)
    .with_column(trip_duration.alias("trip_duration"))
    .filter(pl.col("trip_duration") > 0)
    .groupby(["vendor_id"])
    .agg(
        [
            (pl.col("trip_distance") / pl.col("trip_duration")).mean().alias("avg_speed"),
            (pl.col("tip_amount") / pl.col("passenger_count")).mean().alias("avg_tip_per_person"),
        ]
    )
).schema == {"vendor_id": pl.Utf8, "avg_speed": pl.Float64, "avg_tip_per_person": pl.Float64}

os.chdir("..")
