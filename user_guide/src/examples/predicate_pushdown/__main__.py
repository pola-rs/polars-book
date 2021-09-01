from ..paths import OUTPUT_BASE_DIR, create_if_not_exists
from .snippet1 import df1
from .snippet1 import q as q1
from .snippet2 import df as df2
from .snippet2 import q as q2

path = create_if_not_exists(f"{OUTPUT_BASE_DIR}/predicate_pushdown")

for n, x in enumerate([q1, q2]):
    x.show_graph(optimized=False, show=False, output_path=f"{path}/graph{n + 1}.png")
    x.show_graph(optimized=True, show=False, output_path=f"{path}/graph{n + 1}-optimized.png")

for n, x in enumerate([df1, df2]):
    with open(f"{path}/output{n + 1}.txt", "w") as f:
        f.write(f"{x}\n")
