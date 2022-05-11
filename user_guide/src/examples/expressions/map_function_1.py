import polars as pl

df = pl.DataFrame(
    {
        "keys": ["a", "a", "b"],
        "values": [10, 7, 1],
    }
)

out = df.groupby("keys", maintain_order=True).agg(
    [
        pl.col("values").map(lambda s: s.shift()).alias("shift_map"),
        pl.col("values").shift().alias("shift_expression"),
    ]
)
