import matplotlib.pyplot as plt
import pandas as pd
import os
import numpy as np

os.makedirs("book/src/img", exist_ok=True)


# with open("data/macro_bench_pandas.txt") as f:
#     pandas = [float(a) for a in f.read().split("\n")]
#
# with open("data/macro_bench_polars.txt") as f:
#     polars = [float(a) for a in f.read().split("\n")]
#
# lib = ["polars", "pandas"]
# x = ["macro"]
#
# plt.figure(figsize=(14, 4))
# plt.suptitle("macro query")
#
# df = pd.DataFrame({"query": x, "polars": polars, "pandas": pandas})
#
# df.plot.bar(x="query", figsize=(14, 6))
# plt.savefig("book/src/img/macro_query.png")


with open("data/pandas_bench_join.txt") as f:
    pandas = [float(a) for a in f.read().split("\n")[:-1]]

with open("data/polars_bench_join.txt") as f:
    polars = [float(a) for a in f.read().split("\n")[:-1]]

x = ["inner", "left", "outer"]

df = pd.DataFrame({"join_type": x, "polars": polars, "pandas": pandas})

df.plot.bar(x="join_type", figsize=(14, 6))
plt.title("join on 80,000 rows")
plt.ylabel("time [μs]")
plt.savefig("book/src/img/join_80_000.png")

with open("data/pandas_bench_csv_read.txt") as f:
    pandas = [float(a) for a in f.read().split("\n")[:-1]]

with open("data/polars_bench_csv_read.txt") as f:
    polars = [float(a) for a in f.read().split("\n")[:-1]]

x = ["100,000", "1,000,000", "10,000,000"]

df = pd.DataFrame(
    {
        "n_rows": x,
        "polars": polars[1:],
        "pandas": pandas[1:],
    }
)

df.plot.bar(x="n_rows", figsize=(14, 6), rot=30)
plt.title("csv parsing")
plt.ylabel("time [μs]")
plt.savefig("book/src/img/csv.png")


def parse_result(f):
    return [float(a) / 1000 for a in f.read().split("\n")[:-1]]


with open("data/pandas_bench_gb.txt") as f:
    pandas = parse_result(f)

with open("data/polars_bench_gb.txt") as f:
    polars = parse_result(f)

sizes = [1e4, 1e5, 1e6, 1e7]
lib = ["polars", "pandas"]
x = np.arange(1, 3)

fig, ax = plt.subplots(1, len(sizes), figsize=(14, 4))
plt.suptitle("Group by on 10 groups")
plt.subplots_adjust(wspace=0.4)
r = 0
ax = ax[None, :]
for i in range(len(polars)):
    c = i
    ca = ax[r, c]

    ca.set_title(f"{int(sizes[i]):,} rows")
    ca.bar(
        x,
        [polars[i], pandas[i]],
        color=["C0", "C1"],
        width=0.4,
        label="int",
    )
    ca.set_xticks(x)
    ca.set_xticklabels(lib)
    ca.set_ylabel("duration [seconds]")
    ca.legend()
plt.savefig("book/src/img/groupby10_.png")

with open("data/pandas_gb_mem.txt") as f:
    pandas = [float(a) for a in f.read().split("\n")[:-1]]

with open("data/polars_gb_mem.txt") as f:
    polars = [float(a) for a in f.read().split("\n")[:-1]]

fig, ax = plt.subplots(1, len(sizes), figsize=(14, 4))
plt.suptitle("Memory usage during Groupby")
plt.subplots_adjust(wspace=0.5, bottom=0.2)
r = 0
ax = ax[None, :]
for i in range(len(polars)):
    c = i
    ca = ax[r, c]

    ca.set_title(f"{int(sizes[i]):,} rows")
    ca.bar(
        x,
        [polars[i], pandas[i]],
        color=["C0", "C1"],
        alpha=0.75,
        width=0.4,
    )
    ca.set_xticks(x)
    ca.set_xticklabels(lib, rotation=30)
    ca.set_ylabel("process memory [GB]")
plt.savefig("book/src/img/groupby10_mem.png")
