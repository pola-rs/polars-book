from .dataset import df_a, df_b

q = df_a.lazy().join(df_b.lazy(), left_on="a", right_on="foo", how="outer")
out = q.collect()
