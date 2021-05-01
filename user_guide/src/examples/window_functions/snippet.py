import polars as pl

dataset = pl.DataFrame(
    {
        "A": [1, 2, 3, 4, 5],
        "fruits": ["banana", "banana", "apple", "apple", "banana"],
        "B": [5, 4, 3, 2, 1],
        "cars": ["beetle", "audi", "beetle", "beetle", "beetle"],
    }
)

q = dataset.lazy().with_columns(
    [
        pl.sum("A").over("fruits").alias("fruit_sum_A"),
        pl.first("B").over("fruits").alias("fruit_first_B"),
        pl.max("B").over("cars").alias("cars_max_B"),
    ]
)

df = q.collect()
