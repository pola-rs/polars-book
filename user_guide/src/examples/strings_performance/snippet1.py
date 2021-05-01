import polars as pl

df1 = pl.DataFrame({"a": ["foo", "bar", "ham"], "b": [1, 2, 3]})
df2 = pl.DataFrame({"a": ["foo", "spam", "eggs"], "c": [3, 2, 2]})

with pl.StringCache():
    df1["a"] = df1["a"].cast(pl.Categorical)
    df2["a"] = df2["a"].cast(pl.Categorical)
