import polars as pl
from polars.lazy import *
import time

t0 = time.time()

left = pl.scan_csv("data/join_left_80000.csv")
right = pl.scan_csv("data/join_right_80000.csv")
other = pl.scan_csv("data/10000000.csv")

q = (
    left.join(right, on="key", how="inner")
    .filter(col("value") > 0.5)
    .with_column((col("value") * 10).cast(int))
    .join(
        other.groupby("groups").agg(pl.sum("values")),
        left_on="value",
        right_on="groups",
        how="inner",
    )
    .select(["key", "values_sum"])
)
print(q._la)
df = q.collect()


t = time.time() - t0
# with open("data/macro_bench_polars.txt", "w") as f:
#     f.write(str(t))
print(df)
print(q.describe_optimized_plan())
