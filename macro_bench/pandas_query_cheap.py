import pandas as pd
import time

t0 = time.time()
left = pd.read_csv("data/join_left_80000.csv")
right = pd.read_csv("data/join_right_80000.csv")
other = pd.read_csv("data/10000000.csv")

df = left.merge(right, on="key", how="inner")

df = df[df["value"] > 0.5]
df["value"] = (df["value"] * 10).astype(int)

other_sum = other.groupby("groups").sum()

df = df.merge(
    other_sum,
    left_on="value",
    right_on="groups",
    how="inner",
)

t = time.time() - t0
with open("data/macro_bench_pandas.txt", "w") as f:
    f.write(str(t))
print(df[["key", "values"]])
