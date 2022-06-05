import polars as pl
from .datatypes import df


colors = pl.DataFrame(
    {
        "id": [1, 2, 3],
        "name": ["blue", "red", "green"],
    }
)
colors = colors.with_column(
    pl.col(
        "name",
    )
    .cast(pl.Categorical)
    .alias("name")
)

df = df.join(
    colors.rename({"id": "color_id", "name": "color_name"}),
    left_on="color",
    right_on="color_name",
    how="left",
)

color_ids = df.color_id.unique()
