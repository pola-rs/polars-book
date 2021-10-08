import numpy as np
import polars as pl

country = [x for i in [4 * [c] for c in ["belgium", "united-kingdom", "china"]] for x in i]
date = ["2020-12-20", "2020-12-21", "2020-12-22", "2020-12-23"]
cumcases = [23, 42, 67, 85]

raw_data = pl.DataFrame(
    {
        "country": country,
        "date": np.hstack([date, date, date]),
        "cumcases": np.hstack([cumcases, [2 * c for c in cumcases], [3 * c for c in cumcases]]),
    }
)

# first parse column as date
# next create a sorting key defined by the group uid + date_integer
# sort all values on the sorting key so that
parsed_sorted = (
    raw_data.lazy()
    .with_column(pl.col("date").str.parse_date(pl.Date))
    .with_column((pl.col("country").cast(str) + pl.lit("-") + pl.col("date").cast(int)).alias("sort_key"))
    .sort("sort_key")
)

df = parsed_sorted.collect()
