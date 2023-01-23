import polars as pl

with_offset = pl.Series(["2020-01-01 00:00:00+01:00"])

with_offset_parsed = with_offset.str.strptime(pl.Datetime, "%Y-%m-%d %H:%M:%S%z")

zulu_time = pl.Series(["2020-01-01 00:00:00Z"])

zulu_time_parsed = zulu_time.str.strptime(pl.Datetime, "%Y-%m-%d %H:%M:%SZ").dt.with_time_zone("UTC")

tz_naive = pl.Series(["2020-01-01 03:00:00"]).str.strptime(pl.Datetime)

tz_aware = tz_naive.dt.with_time_zone("Europe/Brussels")

out_1 = tz_naive.dt.with_time_zone("Europe/Brussels")

out_2 = tz_naive.dt.with_time_zone("UTC").dt.with_time_zone("Europe/Brussels")

out_3 = tz_aware.dt.with_time_zone("US/Pacific")

out_4 = tz_aware.dt.cast_time_zone("US/Pacific")

out_5 = tz_aware.dt.cast_time_zone("UTC").dt.with_time_zone(None)
