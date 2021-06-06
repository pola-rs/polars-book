import polars as pl

dataset = pl.DataFrame({"a": "The man that ate a whole cake".split(" ")})

df = (
    dataset.lazy().filter(pl.col("a").str.contains(r"(?i)^the$|^a$").is_not()).collect()
)
