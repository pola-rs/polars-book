import polars as pl

df = pl.DataFrame({"shakespeare": "All that glitters is not gold".split(" ")})

df = df.with_column(pl.col("shakespeare").str.lengths().alias("letter_count"))
