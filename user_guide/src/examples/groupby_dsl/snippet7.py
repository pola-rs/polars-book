import polars as pl

from .dataset import dataset


def get_person() -> pl.Expr:
    return pl.col("first_name") + pl.lit(" ") + pl.col("last_name")


q = (
    dataset.lazy()
    .sort("birthday")
    .groupby(["state"])
    .agg(
        [
            get_person().first().alias("youngest"),
            get_person().last().alias("oldest"),
            get_person().sort().first().alias("alphabetical_first"),
            pl.col("gender").sort_by("first_name").first().alias("gender"),
        ]
    )
    .sort("state")
    .limit(5)
)

df = q.collect()
