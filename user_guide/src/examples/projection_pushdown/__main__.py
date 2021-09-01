from ..paths import OUTPUT_BASE_DIR, create_if_not_exists
from .snippet import dataset, df1

path = create_if_not_exists(f"{OUTPUT_BASE_DIR}/projection_pushdown")

dataset.show_graph(optimized=False, show=False, output_path=f"{path}/graph.png")
dataset.show_graph(optimized=True, show=False, output_path=f"{path}/graph-optimized.png")

with open(f"{path}/output.txt", "w") as f:
    f.write(f"{df1}\n")
