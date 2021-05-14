from .dataset import df

out = df.melt(id_vars=["A", "B"], value_vars=["C", "D"])
