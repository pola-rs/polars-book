import polars as pl

df = pl.DataFrame({"a": "The man that ate a whole cake".split(" ")})

df = df.filter(pl.col("a").str.contains(r"(?i)^the$|^a$").is_not())
