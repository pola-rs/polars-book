import polars as pl

# DataFrames for semi & anti joins
df_cars = pl.DataFrame(
    {
        "id": ["a", "b", "c"],
        "make": ["ford", "toyota", "bmw"],
    }
)
df_repairs = pl.DataFrame(
    {
        "id": ["c", "c"],
        "cost": [100, 200],
    }
)
df_inner_join = df_cars.join(df_repairs, on="id", how="inner")
df_semi_join = df_cars.join(df_repairs, on="id", how="semi")
df_anti_join = df_cars.join(df_repairs, on="id", how="anti")
