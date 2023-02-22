from .join_df1 import df1
from .join_df2 import df2

out = df1.join(df2, left_on="a", right_on="x")
