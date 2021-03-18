import polars as pl

df = pl.DataFrame(
    {
        "A": [1, 2, 3, 4, 5],
        "fruits": ["banana", "banana", "apple", "apple", "banana"],
        "B": [5, 4, 3, 2, 1],
        "cars": ["beetle", "audi", "beetle", "beetle", "beetle"],
    }
)

windows = df.lazy().with_columns(
    [
        pl.sum("A").over("fruits").alias("fruit_sum_A"),
        pl.first("B").over("fruits").alias("fruit_first_B"),
        pl.max("B").over("cars").alias("cars_max_B"),
    ]
)


if __name__ == "__main__":
    with open("book/src/outputs/how_can_i_apply_window_functions_0.txt", "w") as f:
        f.write(str(df))

    with open("book/src/outputs/how_can_i_apply_window_functions_1.txt", "w") as f:
        f.write(str(windows.collect()))
