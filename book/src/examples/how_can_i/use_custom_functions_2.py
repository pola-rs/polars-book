import polars as pl
from polars.lazy import *

my_map = {1: "foo", 2: "bar", 3: "ham", 4: "spam", 5: "eggs"}

df = pl.DataFrame({"foo": [1, 2, 3, 4, 5]})

# create a udf
def my_custom_func(s: Series) -> Series:
    return s.apply(lambda x: my_map[x])


# run query with udf
out = df.lazy().with_column(col("foo").map(my_custom_func).alias("mapped"))

if __name__ == "__main__":
    with open("book/src/outputs/how_can_i_use_custom_functions_2.txt", "w") as f:
        f.write(str(out.collect()))
