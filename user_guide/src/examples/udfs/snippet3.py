import polars as pl

my_map = {1: "foo", 2: "bar", 3: "ham", 4: "spam", 5: "eggs"}

dataset = pl.DataFrame({"foo": [1, 2, 3, 4, 5]})


def my_custom_func(s: pl.Series) -> pl.Series:
    return s.apply(lambda x: my_map[x])


q = dataset.lazy().with_column(pl.col("foo").map(my_custom_func).alias("mapped"))

df = q.collect()
