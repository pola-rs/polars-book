from ..paths import OUTPUT_BASE_DIR, create_if_not_exists
from .snippet1 import dataset as dataset1
from .snippet2 import dataset as dataset2

path = create_if_not_exists(f"{OUTPUT_BASE_DIR}/head")

for n, x in enumerate([dataset1, dataset2]):
    with open(f"{path}/output{n + 1}.txt", "w") as f:
        f.write(f"{x.head()}\n")
