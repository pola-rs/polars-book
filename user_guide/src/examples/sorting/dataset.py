import numpy as np
import polars as pl

df = pl.DataFrame({"a": np.arange(1, 4), "b": ["a", "a", "b"]})
