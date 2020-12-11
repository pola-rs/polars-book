import pandas as pd
import time

t0 = time.time()
reddit = pd.read_csv("data/reddit.csv", nrows=int(1e7))
optimal = False

reddit = reddit[reddit["comment_karma"] > 0]
reddit = reddit[reddit["link_karma"] > 0]
reddit = reddit[reddit["name"].str.contains(r"^a")]
# Note uncomment the string comparison.

# if optimal:
#     mask = (
#         (reddit["comment_karma"] > 0)
#         & (reddit["link_karma"] > 0)
#         & reddit["name"].str.contains(r"^a")
#     )
#     reddit = reddit[mask]
# else:
#     reddit = reddit[reddit["comment_karma"] > 0]
#     reddit = reddit[reddit["link_karma"] > 0]
#     reddit = reddit[reddit["name"].str.contains(r"^a")]

print(time.time() - t0)
print(reddit)
