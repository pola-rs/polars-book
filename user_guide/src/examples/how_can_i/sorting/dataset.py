import polars as pl
import numpy as np

df = pl.DataFrame({"a": np.arange(1, 4), "b": ["a", "a", "b"]})
