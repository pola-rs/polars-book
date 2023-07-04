# --8<-- [start:setup]

import polars as pl
import numpy as np

np.random.seed(12)
# --8<-- [end:setup]


# --8<-- [start:dataframe]
df = pl.DataFrame(
    {
        "nrs": [1, 2, 3, None, 5],
        "names": ["foo", "ham", "spam", "egg", "spam"],
        "random": np.random.rand(5),
        "groups": ["A", "A", "B", "C", "B"],
    }
)
print(df)
# --8<-- [end:dataframe]

# --8<-- [start:all]

df_all = df.select([pl.col("*")])

# Is equivalent to
df_all = df.select([pl.all()])
print(df_all)
# --8<-- [end:all]


# --8<-- [start:exclude]

df_exclude = df.select([pl.exclude("groups")])
print(df_exclude)
# --8<-- [end:exclude]

# --8<-- [start:selectors_df]
from datetime import date, datetime

sdf = pl.DataFrame(
    {
        "id": [9, 4, 2],
        "place": ["Mars", "Earth", "Saturn"],
        "date": pl.date_range(date(2022, 1, 1), date(2022, 1, 3), "1d", eager=True),
        "sales": [33.4, 2142134.1, 44.7],
        "has_people": [False, True, False],
        "logged_at": pl.date_range(
            datetime(2022, 12, 1), datetime(2022, 12, 1, 0, 0, 2), "1s", eager=True
        ),
    }
).with_row_count("rn")
print(sdf)
# --8<-- [end:selectors_df]

# --8<-- [start:selectors_intro]
import polars.selectors as cs

out = sdf.select(cs.integer(), cs.string())
print(out)
# --8<-- [end:selectors_intro]

# --8<-- [start:selectors_diff]
out = sdf.select(cs.numeric() - cs.first())
print(out)
# --8<-- [end:selectors_diff]

# --8<-- [start:selectors_union]
out = sdf.select(cs.by_name("rn") | ~cs.numeric())
print(out)
# --8<-- [end:selectors_union]

# --8<-- [start:selectors_by_name]
out = sdf.select(cs.contains("rn"), cs.matches(".*_.*"))
print(out)
# --8<-- [end:selectors_by_name]


# --8<-- [start:selectors_to_expr]
out = sdf.select(cs.temporal().as_expr().dt.to_string("%Y-%h-%d"))
print(out)
# --8<-- [end:selectors_to_expr]

# --8<-- [start:samename]
df_samename = df.select([pl.col("nrs") + 5])
print(df_samename)
# --8<-- [end:samename]


# --8<-- [start:samenametwice]
try:
    df_samename2 = df.select([pl.col("nrs") + 5, pl.col("nrs") - 5])
    print(df_samename2)
except Exception as e:
    print(e)
# --8<-- [end:samenametwice]

# --8<-- [start:samenamealias]
df_alias = df.select(
    [
        (pl.col("nrs") + 5).alias("nrs + 5"),
        (pl.col("nrs") - 5).alias("nrs - 5"),
    ]
)
print(df_alias)
# --8<-- [end:samenamealias]

# --8<-- [start:countunique]
df_alias = df.select(
    [
        pl.col("names").n_unique().alias("unique"),
        pl.approx_unique("names").alias("unique_approx"),
    ]
)
print(df_alias)
# --8<-- [end:countunique]

# --8<-- [start:conditional]
df_conditional = df.select(
    [
        pl.col("nrs"),
        pl.when(pl.col("nrs") > 2)
        .then(pl.lit(True))
        .otherwise(pl.lit(False))
        .alias("conditional"),
    ]
)
print(df_conditional)
# --8<-- [end:conditional]
