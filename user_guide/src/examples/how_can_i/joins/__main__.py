from user_guide.src.examples.paths import OUTPUT_BASE_DIR, create_if_not_exists
from .dataset import df_a as dataset_a, df_b as dataset_b

path = create_if_not_exists(f"{OUTPUT_BASE_DIR}/how_can_i/joins")

with open(f"{path}/dataset_a.txt", "w") as f:
    f.write(f"{dataset_a}\n")

with open(f"{path}/dataset_b.txt", "w") as f:
    f.write(f"{dataset_b}\n")

from .eager import out

with open(f"{path}/eager.txt", "w") as f:
    f.write(f"{out}\n")

from .lazy import out

with open(f"{path}/lazy.txt", "w") as f:
    f.write(f"{out}\n")
