import polars as pl

ts = ['2021-03-27T23:59:59+01:00', '2021-03-28T23:59:59+02:00']

mixed_parsed = (
    pl.Series(ts)
    .str.strptime(pl.Datetime, '%+', utc=True)
    .dt.with_time_zone('Europe/Brussels')
)
