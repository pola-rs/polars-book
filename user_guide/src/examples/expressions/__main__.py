from ..paths import OUTPUT_BASE_DIR, create_if_not_exists
from .dataset import df as dataset
from .select_context_1 import df as sc1
from .expressions_examples_1 import df as e1
from .expressions_examples_2 import df as e2
from .expressions_examples_3 import df as e3
from .expressions_examples_4 import df as e4
from .agg_context_1 import df as ac1
from .with_column_context_1 import df as c2
from .window import df as w0
from .fold_1 import out as fold_out_1
from .fold_2 import out as fold_out_2
from .fold_3 import out as fold_out_3
from .window_1 import df as w1
from .window_2 import out as w2
from .window_3 import out as w3
from .numpy_ufunc import out as np_uf1

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

with open(f"{path}/window_0.txt", "w") as f:
    f.write(f"{w0}\n")

with open(f"{path}/folds_1.txt", "w") as f:
    f.write(f"{fold_out_1}\n")

with open(f"{path}/folds_2.txt", "w") as f:
    f.write(f"{fold_out_2}\n")

with open(f"{path}/folds_3.txt", "w") as f:
    f.write(f"{fold_out_3}\n")

with open(f"{path}/window_1.txt", "w") as f:
    f.write(f"{w1}\n")

with open(f"{path}/window_2.txt", "w") as f:
    f.write(f"{w2}\n")

with open(f"{path}/window_3.txt", "w") as f:
    f.write(f"{w3}\n")

with open(f"{path}/np_ufunc_1.txt", "w") as f:
    f.write(f"{np_uf1}\n")
