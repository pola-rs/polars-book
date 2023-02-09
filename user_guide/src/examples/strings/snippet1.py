import polars as pl

df = pl.DataFrame({"shakespeare": "All that glitters is not gold".split(" ")})

df = df.with_columns(pl.col("shakespeare").str.lengths().alias("letter_count"))
