from ..paths import OUTPUT_BASE_DIR, create_if_not_exists
from .snippet1 import s as s1

path = create_if_not_exists(f"{OUTPUT_BASE_DIR}/udfs")

for n, x in enumerate([s1]):
    with open(f"{path}/output{n + 1}.txt", "w") as f:
        f.write(f"{x}\n")
