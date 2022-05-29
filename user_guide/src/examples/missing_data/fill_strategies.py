import polars as pl

df = pl.DataFrame({"col1": [1, 2, 3], "col2": [1, None, 3]})

fillLiteral = df.with_column(pl.col("col2").fill_null(pl.lit(2)))

fillForward = df.with_column(pl.col("col2").fill_null("forward"))

fillMedian = df.with_column(pl.col("col2").fill_null(pl.median("col2")))

fillInterpolation = df.with_column(pl.col("col2").interpolate())

dfNaN = pl.DataFrame({"col1": [1, 2, 3], "col2": [1.0, float("nan"), 3.0]})
meanNaN = dfNaN.with_column(pl.col("col2").fill_nan(None).alias("col2")).mean()
