import polars as pl

df = pl.read_csv("./data/reddit.csv", stop_after_n_rows=10)
df.head()

with open("book/src/outputs/head_reddit.txt", "w") as f:
    f.write(str(df.head()))

df = pl.read_csv(
    "./data/runescape.csv",
    has_headers=False,
    stop_after_n_rows=10,
)
df.head()

with open("book/src/outputs/head_runescape.txt", "w") as f:
    f.write(str(df.head()))
