import numpy as np
from pandas.util.testing import rands
import polars as pl

data_dir = "./data"

groups = np.arange(10)
str_groups = np.array(list("0123456789"))
np.random.seed(1)

for size in [1e4, 1e5, 1e6, 1e7]:
    print(f"create groupby data for {int(size)} rows")
    size = int(size)
    g = np.random.choice(groups, size)
    sg = np.random.choice(str_groups, size)
    v = np.random.randn(size)
    df = pl.DataFrame({"groups": g, "values": v, "str": sg})
    df.to_csv(f"{data_dir}/{size}.csv")

print("groupby data created")

# Join benchmark data
# https://wesmckinney.com/blog/high-performance-database-joins-with-pandas-dataframe-more-benchmarks/
# https://github.com/wesm/pandas/blob/23669822819808bbaeb6ea36a6b2ef98026884db/bench/bench_merge_sqlite.py
N = 10000
indices = np.array([rands(10) for _ in range(N)], dtype="O")
indices2 = np.array([rands(10) for _ in range(N)], dtype="O")
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

left.to_csv(data_dir + "/join_left_80000.csv")
right.to_csv(data_dir + "/join_right_80000.csv")

print("join data created")
