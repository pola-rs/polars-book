import polars as pl

pl.DataFrame({"foo": ["a", "b", "c"], "bar": [0, 1, 2]}).lazy().with_columns(pl.col("bar").round(0))
