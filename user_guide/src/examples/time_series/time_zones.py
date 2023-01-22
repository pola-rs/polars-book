import polars as pl

tz_naive = pl.Series(['2020-01-01 03:00:00']).str.strptime(pl.Datetime)

tz_aware = tz_naive.dt.with_time_zone('Europe/Brussels')

out_1 = tz_naive.dt.with_time_zone('Europe/Brussels')

out_2 = tz_naive.dt.with_time_zone('UTC').with_time_zone('Europe/Brussels')

out_3= tz_aware.dt.with_time_zone('US/Pacific')

out_4 = tz_aware.dt.cast_time_zone('US/Pacific')

out_5 = tz_aware.dt.cast_time_zone('UTC').dt.with_time_zone(None)
