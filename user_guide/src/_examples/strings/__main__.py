from ..paths import OUTPUT_BASE_DIR, create_if_not_exists
from .snippet1 import df as df1
from .snippet2 import df as df2

path = create_if_not_exists(f"{OUTPUT_BASE_DIR}/strings")

for n, x in enumerate([df1, df2]):
    with open(f"{path}/output{n + 1}.txt", "w") as f:
        f.write(f"{x}\n")
