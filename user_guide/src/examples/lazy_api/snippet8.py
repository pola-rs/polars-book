import polars as pl

lazy_eager_query = (
    pl.DataFrame({"id": ["a", "b", "c"], "month": ["jan", "feb", "mar"], "values": [0, 1, 2]})
    .lazy()
    .with_columns((2 * pl.col("values")).alias("double_values"))
    .collect()
    .pivot(index="id", columns="month", values="double_values")
    .lazy()
    .filter(pl.col("mar").is_null())
    .collect()
)
