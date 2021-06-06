from datetime import datetime

import polars as pl

from .dataset import dataset


def compute_age() -> pl.Expr:
    # Date64 is time in ms
    ms_to_year = 1e3 * 3600 * 24 * 365
    return (
        pl.lit(datetime(2021, 1, 1)) - pl.col("birthday").str.parse_date(pl.Date32)
    ) / (ms_to_year)


def avg_birthday(gender: str) -> pl.Expr:
    return (
        compute_age()
        .filter(pl.col("gender") == gender)
        .mean()
        .alias(f"avg {gender} birthday")
    )


q = (
    dataset.lazy()
    .groupby(["state"])
    .agg(
        [
            avg_birthday("M"),
            avg_birthday("F"),
            (pl.col("gender") == "M").sum().alias("# male"),
            (pl.col("gender") == "F").sum().alias("# female"),
        ]
    )
    .limit(5)
)

df = q.collect()
