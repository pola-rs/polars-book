from .dataset import df_a, df_b

out = df_a.join(df_b, left_on=["a", "b"], right_on=["foo", "bar"], how="left")
