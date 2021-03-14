import polars as pl
from polars.lazy import *
import numpy as np

np.random.seed(1)

df = pl.DataFrame({"foo": np.arange(10), "bar": np.random.rand(10)})

# create a udf
def my_custom_func(s: Series) -> Series:
    return np.exp(s) / np.log(s)


# a simple wrapper that take a function and sets output type
my_udf = udf(my_custom_func, output_type=pl.Float64)

# run query with udf
out = df.lazy().filter(col("bar").map(my_udf) > -1)

if __name__ == "__main__":
    with open("book/src/outputs/how_can_i_use_custom_functions_1.txt", "w") as f:
        f.write(str(out.collect()))
