import polars as pl


q6 = pl.DataFrame({"foo": ["a", "b", "c"], "bar": [0.0, 0.1, 0.2]}).lazy().with_columns(rounded=pl.col("foo").round(0))
