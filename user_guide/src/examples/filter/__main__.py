from ..paths import OUTPUT_BASE_DIR, create_if_not_exists
from .lazy import out

path = create_if_not_exists(f"{OUTPUT_BASE_DIR}/filter")

with open(f"{path}/filter.txt", "w") as f:
    f.write(f"{out}\n")
