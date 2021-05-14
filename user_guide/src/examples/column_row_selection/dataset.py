import numpy as np
import polars as pl

np.random.seed(42)

df = pl.DataFrame(
    {
        "a": [1, 2, 3, None, 5],
        "b": ["foo", "ham", "spam", "egg", None],
        "c": np.random.rand(5),
        "d": ["a", "b", "c", "d", "e"],
    }
)
