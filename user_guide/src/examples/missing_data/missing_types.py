import polars as pl
import numpy as np

df = pl.DataFrame({"colName": [1, None]})

nullCountDf = df.null_count()

isNullSeries = df.select(pl.col("colName").is_null())

dfNaN = pl.DataFrame({"colName": [1.0, np.NaN, float("nan")]})
