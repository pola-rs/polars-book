from ..paths import OUTPUT_BASE_DIR, create_if_not_exists
from .dataset import df_a as dataset_a
from .dataset import df_b as dataset_b
from .eager import out as eout
from .lazy import out as lout

path = create_if_not_exists(f"{OUTPUT_BASE_DIR}/join")

with open(f"{path}/dataset_a.txt", "w") as f:
    f.write(f"{dataset_a}\n")

with open(f"{path}/dataset_b.txt", "w") as f:
    f.write(f"{dataset_b}\n")

with open(f"{path}/eager.txt", "w") as f:
    f.write(f"{eout}\n")

with open(f"{path}/lazy.txt", "w") as f:
    f.write(f"{lout}\n")
