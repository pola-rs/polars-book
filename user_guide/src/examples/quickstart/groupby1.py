from .dataframe3 import df

out = df.groupby("y", maintain_order=True).count()
