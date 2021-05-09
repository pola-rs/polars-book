from user_guide.src.examples.paths import OUTPUT_BASE_DIR, create_if_not_exists
from .dataset import df as dataset

path = create_if_not_exists(f"{OUTPUT_BASE_DIR}/how_can_i/pivot")

with open(f"{path}/dataset.txt", "w") as f:
    f.write(f"{dataset}\n")

from .eager import out

with open(f"{path}/eager.txt", "w") as f:
    f.write(f"{out}\n")

from .lazy import out

with open(f"{path}/lazy.txt", "w") as f:
    f.write(f"{out}\n")
