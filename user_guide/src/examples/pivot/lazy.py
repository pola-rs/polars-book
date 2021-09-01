from .dataset import df

q = df.lazy().map(lambda df: df.groupby("foo").pivot(pivot_column="bar", values_column="N").first())
out = q.collect()
