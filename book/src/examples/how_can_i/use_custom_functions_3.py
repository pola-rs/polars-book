import polars as pl
from polars.lazy import *


df = pl.DataFrame(
    {
        "A": [1, 2, 3, 4, 5],
        "fruits": ["banana", "banana", "apple", "apple", "banana"],
        "B": [5, 4, 3, 2, 1],
        "cars": ["beetle", "audi", "beetle", "beetle", "beetle"],
    }
)

# two ways to determine the length groups.
out = (
    df.lazy()
    .groupby("fruits")
    .agg(
        [
            col("cars").apply(lambda groups: groups.len()).alias("custom_1"),
            col("cars").apply(lambda groups: groups.len()).alias("custom_2"),
            pl.count("cars"),
        ]
    )
)


if __name__ == "__main__":
    with open("book/src/outputs/how_can_i_use_custom_functions_3.txt", "w") as f:
        f.write(str(out.collect()))
