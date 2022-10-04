import polars as pl

df = pl.DataFrame(
    {
        "col1": [1, 2, 3],
        "col2": [1, None, 3],
    },
)

fill_literal_df = (
    df.with_column(
        pl.col("col2").fill_null(
            pl.lit(2),
        ),
    ),
)

fill_forward_df = df.with_column(
    pl.col("col2").fill_null(strategy="forward"),
)

fill_median_df = df.with_column(
    pl.col("col2").fill_null(pl.median("col2")),
)

fill_interpolation_df = df.with_column(
    pl.col("col2").interpolate(),
)

nan_df = pl.DataFrame(
    {
        "value": [1.0, float("nan"), float("nan"), 3.0],
    },
)
mean_nan_df = nan_df.with_column(
    pl.col("value").fill_nan(None).alias("value"),
).mean()
