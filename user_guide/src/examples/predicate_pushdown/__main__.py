from ..paths import OUTPUT_BASE_DIR, create_if_not_exists
from .snippet1 import q1 as q1
from .snippet2 import q2 as q2

path = create_if_not_exists(f"{OUTPUT_BASE_DIR}/predicate_pushdown")

for n, x in enumerate([q1, q2]):
    x.show_graph(optimized=False, show=False, output_path=f"{path}/graph{n + 1}.png")
    x.show_graph(optimized=True, show=False, output_path=f"{path}/graph{n + 1}-optimized.png")

df1 = q1.fetch(int(1e7))
df2 = q2.fetch(int(1e7))
for n, x in enumerate([df1, df2]):
    with open(f"{path}/output{n + 1}.txt", "w") as f:
        f.write(f"{x}\n")
