import polars as pl
import numpy as np
from datetime import datetime, timedelta

df = pl.DataFrame({"a": np.arange(0, 8), 
                   "b": np.random.rand(8), 
                   "c": [datetime(2022, 12, 1) + timedelta(days=idx) for idx in range(8)],
                   "d": [1, 2.0, np.NaN, np.NaN, 0, -5, -42, None]
                  })