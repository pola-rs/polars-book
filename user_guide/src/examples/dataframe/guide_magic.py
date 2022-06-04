from datetime import datetime


# DAYS = N; generate list of sequentially valid days (as datetimes)
DAYS, MAX_MONTHS, MAX_DAYS, MAX_YEARS = 1000, 12, 28, float("inf")


def datepart(day: int, maximum: int) -> int:
    return int(day % maximum) + 1


y, m, d = 2022, 1, 1
my_datetime_list = list(
    datetime(
        datepart((y + (n // 365)), MAX_YEARS),
        datepart((m + (n + 1)), MAX_MONTHS),
        datepart((n + 1), MAX_DAYS),
    )
    for n in range(DAYS)
)
