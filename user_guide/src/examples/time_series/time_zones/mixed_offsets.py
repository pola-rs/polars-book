import polars as pl

data = [
    "2021-03-27T00:00:00+0100",
    "2021-03-28T00:00:00+0100",
    "2021-03-29T00:00:00+0200",
    "2021-03-30T00:00:00+0200",
]
mixed_parsed = (
    pl.Series(data)
    .str.strptime(pl.Datetime, fmt="%Y-%m-%dT%H:%M:%S%z", utc=True)
    .dt.convert_time_zone("Europe/Brussels")
)
