import polars as pl

my_map = {1: "foo", 2: "bar", 3: "ham", 4: "spam", 5: "eggs"}

s = pl.Series("a", [1, 2, 3, 4, 5])
s = s.apply(lambda x: my_map[x])


if __name__ == "__main__":
    with open("book/src/outputs/how_can_i_use_custom_functions_0.txt", "w") as f:
        f.write(str(s))
