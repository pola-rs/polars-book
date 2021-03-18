import polars as pl
from polars.lazy import col

df = pl.DataFrame(
    {"date": ["2020-01-02", "2020-01-03", "2020-01-04"], "index": [1, 2, 3]}
)

parsed = df.lazy().with_column(
    col("date").str_parse_date(pl.datatypes.Date32, "%Y-%m-%d")
)

if __name__ == "__main__":
    with open("book/src/outputs/how_can_i_parse_dates_0.txt", "w") as f:
        f.write(str(df))
    with open("book/src/outputs/how_can_i_parse_dates_1.txt", "w") as f:
        f.write(str(parsed.collect()))
