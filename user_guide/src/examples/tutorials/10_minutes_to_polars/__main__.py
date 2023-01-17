from ...paths import OUTPUT_BASE_DIR, create_if_not_exists
from .creating_a_dataframe import df

path = create_if_not_exists(f"{OUTPUT_BASE_DIR}/10-minutes-to-polars")

with open(f"{path}/output.txt", "w") as f:
    f.write(f"{df.head(3)}\n")
