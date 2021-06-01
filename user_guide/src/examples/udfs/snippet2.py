import numpy as np
import polars as pl

np.random.seed(1)

dataset = pl.DataFrame({"foo": np.arange(10), "bar": np.random.rand(10)})


def my_custom_func(s: pl.Series) -> pl.Series:
    return np.exp(s) / np.log(s)


# simple wrapper that take a function and sets output type
my_udf = pl.udf(my_custom_func, return_dtype=pl.Float64)

q = dataset.lazy().filter(pl.col("bar").map(my_udf) > -1)

df = q.collect()
