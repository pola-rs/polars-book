import polars as pl

df_colors = pl.DataFrame(
    {
        "color": ["red", "blue", "green"],
    }
)
df_sizes = pl.DataFrame(
    {
        "size": ["S", "M", "L"],
    }
)
df_cross_join = df_colors.join(df_sizes, how="cross")
