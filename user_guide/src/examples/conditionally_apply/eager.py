from .dataset import df

df = df.clone()
mask = df["range"] >= 5
df[mask, "range"] = 12
