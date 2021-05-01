import polars as pl

dataset = pl.DataFrame(
    {"date": ["2020-01-02", "2020-01-03", "2020-01-04"], "index": [1, 2, 3]}
)

q = dataset.lazy().with_column(
    pl.col("date").str_parse_date(pl.datatypes.Date32, "%Y-%m-%d")
)

df = q.collect()
