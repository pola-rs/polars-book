import pandas as pd
import time

t0 = time.time()

reddit = pd.read_csv("data/reddit.csv", nrows=int(1e7))
runestar = pd.read_csv("data/runescape.csv", nrows=int(1e7), names=["name"])

reddit = reddit[reddit["comment_karma"] > 0]
reddit = reddit[reddit["link_karma"] > 0]
reddit = reddit[reddit["name"].str.contains(r"^a")]

joined = reddit.merge(runestar, on="name", how="inner")

df = joined[["name", "comment_karma", "link_karma"]]

print(time.time() - t0)
print(df)
