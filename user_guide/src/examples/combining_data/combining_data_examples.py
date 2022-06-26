import polars as pl

df_cars = pl.DataFrame(
    {
        "id": ["a", "b", "c"],
        "make": ["ford", "toyota", "bmw"],
    }
)
df_repairs = pl.DataFrame(
    {
        "id": ["c", "c"],
        "cost": [100, 200],
    }
)
df_cars.join(df_repairs, on="id", how="inner")
df_cars.join(df_repairs, on="id", how="semi")
df_cars.join(df_repairs, on="id", how="anti")

from datetime import datetime

df_trades = pl.DataFrame(
    {
        "time": [
            datetime(2020, 5, 1, 9, 0, 1),
            datetime(2020, 5, 1, 9, 0, 1),
            datetime(2020, 5, 1, 9, 0, 3),
            datetime(2020, 5, 1, 9, 0, 6),
        ],
        "stock": ["A", "B", "B", "C"],
        "trade": [101, 299, 301, 500],
    }
)

df_quotes = pl.DataFrame(
    {
        "time": [
            datetime(2020, 5, 1, 9, 0, 0),
            datetime(2020, 5, 1, 9, 0, 2),
            datetime(2020, 5, 1, 9, 0, 4),
            datetime(2020, 5, 1, 9, 0, 6),
        ],
        "stock": ["A", "B", "C", "A"],
        "quote": [100, 300, 501, 102],
    }
)
df_trades.join_asof(df_quotes, on="time", by="stock")
df_trades.join_asof(df_quotes, on="time", by="stock", strategy="forward")
df_trades.join_asof(df_quotes, on="time", by="stock", tolerance="1m")
