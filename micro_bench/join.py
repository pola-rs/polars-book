import pandas as pd
import datetime
import numpy as np
import pypolars as pl

left = pd.read_csv("data/join_left_80000.csv")
right = pd.read_csv("data/join_right_80000.csv")

print("pandas")
fw = open("data/pandas_bench_join.txt", "w")

durations = []
for _ in range(10):
    t0 = datetime.datetime.now()
    joined = left.merge(right, on="key", how="inner")
    duration = datetime.datetime.now() - t0
    durations.append(duration.microseconds)
mean = np.mean(durations)
fw.write(f"{mean}\n")
print("inner join {} μs".format(mean))
print("shape:", joined.shape)


durations = []
for _ in range(10):
    t0 = datetime.datetime.now()
    joined = left.merge(right, on="key", how="left")
    duration = datetime.datetime.now() - t0
    durations.append(duration.microseconds)
mean = np.mean(durations)
fw.write(f"{mean}\n")
print("left join {} μs".format(mean))
print("shape:", joined.shape)

durations = []
for _ in range(10):
    t0 = datetime.datetime.now()
    joined = left.merge(right, on="key", how="outer")
    duration = datetime.datetime.now() - t0
    durations.append(duration.microseconds)
mean = np.mean(durations)
fw.write(f"{mean}\n")
print("outer join {} μs".format(mean))
print("shape:", joined.shape)

left = pl.read_csv("data/join_left_80000.csv")
right = pl.read_csv("data/join_right_80000.csv")

print("polars")
fw = open("data/polars_bench_join.txt", "w")

durations = []
for _ in range(10):
    t0 = datetime.datetime.now()
    joined = left.join(right, on="key", how="inner")
    duration = datetime.datetime.now() - t0
    durations.append(duration.microseconds)
mean = np.mean(durations)
fw.write(f"{mean}\n")
print("inner join {} μs".format(mean))
print("shape:", joined.shape)


durations = []
for _ in range(10):
    t0 = datetime.datetime.now()
    joined = left.join(right, on="key", how="left")
    duration = datetime.datetime.now() - t0
    durations.append(duration.microseconds)
mean = np.mean(durations)
fw.write(f"{mean}\n")
print("left join {} μs".format(mean))
print("shape:", joined.shape)

durations = []
for _ in range(10):
    t0 = datetime.datetime.now()
    joined = left.join(right, on="key", how="outer")
    duration = datetime.datetime.now() - t0
    durations.append(duration.microseconds)
mean = np.mean(durations)
fw.write(f"{mean}\n")
print("outer join {} μs".format(mean))
print("shape:", joined.shape)
