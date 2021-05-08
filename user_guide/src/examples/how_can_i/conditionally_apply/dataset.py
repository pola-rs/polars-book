import polars as pl
import numpy as np

df = pl.DataFrame({"range": np.arange(10), "left": ["foo"] * 10, "right": ["bar"] * 10})
