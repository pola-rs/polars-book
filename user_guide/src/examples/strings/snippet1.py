import polars as pl

dataset = pl.DataFrame({"shakespeare": "All that glitters is not gold".split(" ")})

df = (
    dataset.lazy()
    .with_column(pl.col("shakespeare").str_lengths().alias("letter_count"))
    .collect()
)
