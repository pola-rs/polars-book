from datetime import datetime

import polars as pl

df = pl.date_range(low=datetime(2021, 1, 1), high=datetime(2021, 12, 31), interval="1d", name="time").to_frame()

out = (
    df.groupby_dynamic("time", every="1mo", period="1mo", closed="left")
    .agg(
        [
            pl.col("time").cumcount().reverse().head(3).alias("day/eom"),
            ((pl.col("time") - pl.col("time").first()).last().dt.days() + 1).alias("days_in_month"),
        ]
    )
    .explode("day/eom")
)
