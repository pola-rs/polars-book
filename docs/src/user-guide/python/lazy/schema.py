import polars as pl

# --8<-- [start:schema]
q3 = pl.DataFrame({"foo": ["a", "b", "c"], "bar": [0, 1, 2]}).lazy()

print(q3.schema)
# --8<-- [end:schema]

# --8<-- [start:typecheck]
pl.DataFrame({"foo": ["a", "b", "c"], "bar": [0, 1, 2]}).lazy().with_columns(pl.col("bar").round(0))
# --8<-- [end:typecheck]

# --8<-- [start:lazyeager]
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
# --8<-- [end:lazyeager]