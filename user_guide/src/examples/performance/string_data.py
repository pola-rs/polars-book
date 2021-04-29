import polars as pl

df_a = pl.DataFrame({"a": ["foo", "bar", "ham"], "b": [1, 2, 3]})
df_b = pl.DataFrame({"a": ["foo", "spam", "eggs"], "c": [3, 2, 2]})

with pl.StringCache():
    df_a["a"] = df_a["a"].cast(pl.Categorical)
    df_b["a"] = df_b["a"].cast(pl.Categorical)


df_a = pl.DataFrame({"a": ["foo", "bar", "ham"], "b": [1, 2, 3]}).lazy()
df_b = pl.DataFrame({"a": ["foo", "spam", "eggs"], "c": [3, 2, 2]}).lazy()

df_a = df_a.with_column(pl.col("a").cast(pl.Categorical))
df_b = df_b.with_column(pl.col("a").cast(pl.Categorical))

df_a.join(df_b, on="a", how="inner")
