"""Small `Python` snippet to generate mock datasets (in CSV format) to be used by the
code examples included in the User Guide."""

import numpy as np
import pandas as pd
import polars as pl

np.random.seed(1)

DATA_DIR = "data"


# GroupBy benchmark data

print("GroupBy data:")

groups = np.arange(10)
str_groups = np.array(list("0123456789"))

for size in np.array([1e4, 1e5, 1e6, 1e7], dtype=int):
    g = np.random.choice(groups, size)
    sg = np.random.choice(str_groups, size)
    v = np.random.randn(size)
    df = pl.DataFrame({"groups": g, "values": v, "str": sg})
    df.to_csv(f"{DATA_DIR}/{size}.csv")
    print(f"  {int(size)} rows of GroupBy data created")

# Join benchmark data
# https://wesmckinney.com/blog/high-performance-database-joins-with-pandas-dataframe-more-benchmarks/
# https://github.com/wesm/pandas/blob/23669822819808bbaeb6ea36a6b2ef98026884db/bench/bench_merge_sqlite.py

print("Join data:")

N = 10000
indices = np.array([pd._testing.rands(10) for _ in range(N)], dtype=str)
indices2 = np.array([pd._testing.rands(10) for _ in range(N)], dtype=str)
key = np.tile(indices[:8000], 10)
key2 = np.tile(indices2[:8000], 10)

left = pl.DataFrame(
    {
        "key": key,
        "key2": key2,
        "value": np.random.randn(80000),
    }
)

right = pl.DataFrame(
    {
        "key": indices[2000:],
        "key2": indices2[2000:],
        "value2": np.random.randn(8000),
    }
)

left.to_csv(f"{DATA_DIR}/join_left_80000.csv")
right.to_csv(f"{DATA_DIR}/join_right_80000.csv")

print(f"  Left data created (shape: {left.shape})")
print(f"  Right data created (shape: {right.shape})")
