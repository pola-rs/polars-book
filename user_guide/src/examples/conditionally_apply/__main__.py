from ..paths import OUTPUT_BASE_DIR, create_if_not_exists
from .dataset import df as dataset
from .lazy import df as ldf

path = create_if_not_exists(f"{OUTPUT_BASE_DIR}/conditionally_apply")

with open(f"{path}/dataset.txt", "w") as f:
    f.write(f"{dataset.head()}\n")

with open(f"{path}/lazy.txt", "w") as f:
    f.write(f"{ldf}\n")
