import polars as pl

lf1 = pl.DataFrame({"a": ["foo", "bar", "ham"], "b": [1, 2, 3]}).lazy()
lf2 = pl.DataFrame({"a": ["foo", "spam", "eggs"], "c": [3, 2, 2]}).lazy()

lf1 = lf1.with_column(pl.col("a").cast(pl.Categorical))
lf2 = lf2.with_column(pl.col("a").cast(pl.Categorical))

lf1.join(lf2, on="a", how="inner")
