from ..paths import OUTPUT_BASE_DIR, create_if_not_exists
from .days_month import out as days_month
from .dynamic_ds import df as dyn_df
from .dynamic_groupby import out as dyn_gb

path = create_if_not_exists(f"{OUTPUT_BASE_DIR}/time_series")

with open(f"{path}/days_month.txt", "w") as f:
    f.write(f"{days_month}\n")

with open(f"{path}/dyn_df.txt", "w") as f:
    f.write(f"{dyn_df}\n")

with open(f"{path}/dyn_gb.txt", "w") as f:
    f.write(f"{dyn_gb}\n")
