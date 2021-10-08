from datetime import datetime

import polars as pl

from .dataset import dataset


def compute_age() -> pl.Expr:
    return (pl.lit(datetime(2021, 1, 1)) - pl.col("birthday")).dt.year()


def avg_birthday(gender: str) -> pl.Expr:
    return compute_age().filter(pl.col("gender") == gender).mean().alias(f"avg {gender} birthday")


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
