from ..paths import OUTPUT_BASE_DIR, create_if_not_exists
from .dataset import df as dataset
from .select_context_1 import df as sc1
from .expressions_examples_1 import df as e1
from .expressions_examples_2 import df as e2
from .expressions_examples_3 import df as e3
from .expressions_examples_4 import df as e4
from .agg_context_1 import df as ac1
from .with_column_context_1 import df as c2
from .window import df as w1

path = create_if_not_exists(f"{OUTPUT_BASE_DIR}/expressions")

with open(f"{path}/dataset.txt", "w") as f:
    f.write(f"{dataset}\n")

with open(f"{path}/select_context_1.txt", "w") as f:
    f.write(f"{sc1}\n")

with open(f"{path}/example_1.txt", "w") as f:
    f.write(f"{e1}\n")

with open(f"{path}/example_2.txt", "w") as f:
    f.write(f"{e2}\n")

with open(f"{path}/example_3.txt", "w") as f:
    f.write(f"{e3}\n")

with open(f"{path}/example_4.txt", "w") as f:
    f.write(f"{e4}\n")

with open(f"{path}/agg_context_1.txt", "w") as f:
    f.write(f"{ac1}\n")

with open(f"{path}/wc_context_1.txt", "w") as f:
    f.write(f"{c2}\n")

with open(f"{path}/window_1.txt", "w") as f:
    f.write(f"{w1}\n")
