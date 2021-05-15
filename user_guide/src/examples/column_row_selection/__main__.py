from ..paths import OUTPUT_BASE_DIR, create_if_not_exists
from .dataset import df

path = create_if_not_exists(f"{OUTPUT_BASE_DIR}/row_col_selection")

with open(f"{path}/col_selection.txt", "w") as f:
    f.write(f"{df[['a','b']]}\n")

with open(f"{path}/row_selection.txt", "w") as f:
    f.write(f"{df[0:2]}\n")
