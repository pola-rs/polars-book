from ..paths import OUTPUT_BASE_DIR, create_if_not_exists
from .snippet1 import df as df1
from .snippet2 import df as df2
from .snippet3 import df as df3
from .snippet4 import df as df4
from .snippet5 import df as df5
from .snippet6 import df as df6
from .snippet7 import df as df7

path = create_if_not_exists(f"{OUTPUT_BASE_DIR}/groupby_dsl")

for n, x in enumerate([df1, df2, df3, df4, df5, df6, df7]):
    with open(f"{path}/output{n + 1}.txt", "w") as f:
        f.write(f"{x}\n")
