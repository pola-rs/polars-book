import polars as pl


df = pl.DataFrame(
    {
        "id": [1, 2, 3],
        "color": ["blue", "red", "green"],
        "size": ["small", "medium", "large"],
    }
)

expression_df = df.filter(pl.col("id") <= 2).select(["id", "color"])

filter_df = df.filter(pl.col("id") <= 2)

multi_filter_df = df.filter((pl.col("id") <= 2) & (pl.col("size") == "small"))

single_select_df = df.select("id")

list_select_df = df.select(["id", "color"])

condition_select_df = df.select(pl.col("^col.*$"))

dtype_select_df = df.select(pl.col(pl.Int64))
