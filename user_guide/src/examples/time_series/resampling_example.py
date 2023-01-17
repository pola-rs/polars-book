from datetime import datetime

import polars as pl

df = pl.DataFrame(
    {
        "time": pl.date_range(low=datetime(2021, 12, 16), high=datetime(2021, 12, 16, 3), interval="30m"),
        "groups": ["a", "a", "a", "b", "b", "a", "a"],
        "values": [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0],
    }
)
out1 = df.upsample(time_column="time", every="15m").fill_null("forward")

out2 = df.upsample(time_column="time", every="15m").interpolate().fill_null("forward")
