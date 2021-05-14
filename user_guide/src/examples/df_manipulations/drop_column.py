from .dataset import df

# drop single column
df = df.drop("d")

# drop multiple columns
df = df.drop(["b", "c"])
