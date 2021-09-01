import polars as pl

df_a = pl.DataFrame({"a": [1, 2, 1, 1], "b": ["a", "b", "c", "c"], "c": [0, 1, 2, 3]})

df_b = pl.DataFrame({"foo": [1, 1, 1], "bar": ["a", "c", "c"], "ham": ["let", "var", "const"]})
