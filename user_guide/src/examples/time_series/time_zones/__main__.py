import polars as pl
from ...paths import OUTPUT_BASE_DIR, create_if_not_exists
from .snippet import time_zones_df, time_zones_operations

path = create_if_not_exists(f"{OUTPUT_BASE_DIR}/time_series/time_zones")

with open(f"{path}/time_zones_df.txt", "w") as f:
    f.write(f"{time_zones_df}\n")

with open(f"{path}/time_zones_operations.txt", "w") as f:
    f.write(f"{time_zones_operations}\n")
