from .dataset import df

out = df.groupby("foo").pivot(pivot_column="bar", values_column="N").first()
