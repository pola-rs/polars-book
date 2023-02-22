from ..paths import OUTPUT_BASE_DIR, create_if_not_exists
from .series_tuple import series
from .dataframe import df

path = create_if_not_exists(f"{OUTPUT_BASE_DIR}/quickstart")

with open(f"{path}/series_tuple.txt", "w") as f:
    f.write(f"{series}\n")

with open(f"{path}/series_list.txt", "w") as f:
    f.write(f"{series}\n")

with open(f"{path}/dataframe.txt", "w") as f:
    f.write(f"{df}\n")