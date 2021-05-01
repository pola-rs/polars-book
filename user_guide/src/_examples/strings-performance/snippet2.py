import polars as pl

df1 = pl.DataFrame({"a": ["foo", "bar", "ham"], "b": [1, 2, 3]}).lazy()
df2 = pl.DataFrame({"a": ["foo", "spam", "eggs"], "c": [3, 2, 2]}).lazy()

df1 = df1.with_column(pl.col("a").cast(pl.Categorical))
df2 = df2.with_column(pl.col("a").cast(pl.Categorical))

df1.join(df2, on="a", how="inner")
