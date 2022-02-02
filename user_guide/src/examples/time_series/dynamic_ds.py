import polars as pl
from datetime import datetime


df = pl.DataFrame(
    {
        "time": pl.date_range(
            low=datetime(2021, 12, 16),
            high=datetime(2021, 12, 16, 3),
            interval="30m",
        ),
        "groups": ["a", "a", "a", "b", "b", "a", "a"],
    }
)
