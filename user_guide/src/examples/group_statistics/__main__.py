from ..paths import OUTPUT_BASE_DIR, create_if_not_exists
from .dataset import df as dataset
from .snippet1 import df as df1
from .snippet2 import df as df2
from .snippet3 import df as df3

path = create_if_not_exists(f"{OUTPUT_BASE_DIR}/group_statistics")

with open(f"{path}/dataset.txt", "w") as f:
    f.write(f"{dataset}\n")

for n, x in enumerate([df1, df2, df3]):
    with open(f"{path}/output{n + 1}.txt", "w") as f:
        f.write(f"{x}\n")
