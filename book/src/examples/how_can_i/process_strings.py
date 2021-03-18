import polars as pl
from polars.lazy import col

df = pl.DataFrame({"shakespeare": "All that glitters is not gold".split(" ")})

str_lengths = df.lazy().with_column(
    col("shakespeare").str_lengths().alias("letter_count")
)

df = pl.DataFrame({"a": "The man that ate a whole cake".split(" ")})

filtered = df.lazy().filter(col("a").str_contains(r"(?i)^the$|^a$").is_not())

if __name__ == "__main__":
    with open("book/src/outputs/how_can_i_process_strings.txt", "w") as f:
        f.write(str(str_lengths.collect()))

    with open("book/src/outputs/how_can_i_process_strings_1.txt", "w") as f:
        f.write(str(filtered.collect()))
