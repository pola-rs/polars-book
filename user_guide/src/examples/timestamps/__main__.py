from ..paths import OUTPUT_BASE_DIR, create_if_not_exists
from .snippet import df

path = create_if_not_exists(f"{OUTPUT_BASE_DIR}/timestamps")

with open(f"{path}/output.txt", "w") as f:
    f.write(f"{df}\n")
