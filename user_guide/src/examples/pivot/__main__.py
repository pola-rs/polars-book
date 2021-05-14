from ..paths import OUTPUT_BASE_DIR, create_if_not_exists
from .dataset import df as dataset
from .eager import out as eout
from .lazy import out as lout

path = create_if_not_exists(f"{OUTPUT_BASE_DIR}/pivot")

with open(f"{path}/dataset.txt", "w") as f:
    f.write(f"{dataset}\n")

with open(f"{path}/eager.txt", "w") as f:
    f.write(f"{eout}\n")

with open(f"{path}/lazy.txt", "w") as f:
    f.write(f"{lout}\n")
