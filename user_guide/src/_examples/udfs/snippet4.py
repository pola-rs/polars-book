import polars as pl

src_df = pl.DataFrame(
    {
        "A": [1, 2, 3, 4, 5],
        "fruits": ["banana", "banana", "apple", "apple", "banana"],
        "B": [5, 4, 3, 2, 1],
        "cars": ["beetle", "audi", "beetle", "beetle", "beetle"],
    }
)

# three ways to determine the length groups
dataset = (
    src_df.lazy()
    .groupby("fruits")
    .agg(
        [
            pl.col("cars").apply(lambda groups: groups.len()).alias("custom_1"),
            pl.col("cars").apply(lambda groups: groups.len()).alias("custom_2"),
            pl.count("cars"),
        ]
    )
)

df = dataset.collect()
