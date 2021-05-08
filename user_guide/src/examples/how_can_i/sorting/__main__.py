from user_guide.src.examples.paths import OUTPUT_BASE_DIR, create_if_not_exists
from .dataset import df as dataset

path = create_if_not_exists(f"{OUTPUT_BASE_DIR}/how_can_i/sorting")

with open(f"{path}/dataset.txt", "w") as f:
    f.write(f"{dataset.head()}\n")

from .eager import df

with open(f"{path}/eager.txt", "w") as f:
    f.write(f"{df}\n")

from .lazy import df

with open(f"{path}/lazy.txt", "w") as f:
    f.write(f"{df}\n")
