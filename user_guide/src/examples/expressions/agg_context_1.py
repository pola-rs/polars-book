from .dataset import df
import polars as pl

out = df.groupby("groups").agg(
    [
        pl.sum("nrs"),  # sum nrs by groups
        pl.col("random").count().alias("count"),  # count group members
        # sum random where name != null
        pl.col("random").filter(pl.col("names").is_not_null()).sum().suffix("_sum"),
        pl.col("names").reverse().alias(("reversed names")),
    ]
)
