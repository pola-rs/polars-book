from ..paths import OUTPUT_BASE_DIR, create_if_not_exists
from .dataset import df as dataset
from .select_context_1 import out as sc1
from .select_context_2 import out as sc2
from .expressions_examples_1 import out as e1
from .expressions_examples_2 import out as e2
from .expressions_examples_3 import out as e3
from .expressions_examples_4 import out as e4
from .agg_context_1 import out as ac1
from .with_column_context_1 import df as c2
from .window import df as w0
from .fold_1 import out as fold_out_1
from .fold_2 import out as fold_out_2
from .fold_3 import out as fold_out_3
from .window_1 import df as w1
from .window_2 import out as w2
from .window_3 import out as w3
from .window_group_1 import filtered as wg1
from .window_group_2 import out as wg2
from .numpy_ufunc import out as np_uf1
from .map_function_1 import out as map_fun_1
from .apply_function_1 import out as apply_fun_1
from .apply_function_2 import out as apply_fun_2
from .apply_function_3 import out as apply_fun_3
from .list_row_wise_1 import grades
from .list_row_wise_2 import out as row_wise_2

path = create_if_not_exists(f"{OUTPUT_BASE_DIR}/expressions")

with open(f"{path}/dataset.txt", "w") as f:
    f.write(f"{dataset}\n")

with open(f"{path}/select_context_1.txt", "w") as f:
    f.write(f"{sc1}\n")

with open(f"{path}/select_context_2.txt", "w") as f:
    f.write(f"{sc2}\n")

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

with open(f"{path}/window_group_1.txt", "w") as f:
    f.write(f"{wg1}\n")

with open(f"{path}/window_group_2.txt", "w") as f:
    f.write(f"{wg2}\n")

with open(f"{path}/np_ufunc_1.txt", "w") as f:
    f.write(f"{np_uf1}\n")

with open(f"{path}/map_fun_1.txt", "w") as f:
    f.write(f"{map_fun_1}\n")

with open(f"{path}/apply_fun_1.txt", "w") as f:
    f.write(f"{apply_fun_1}\n")

with open(f"{path}/apply_fun_2.txt", "w") as f:
    f.write(f"{apply_fun_2}\n")

with open(f"{path}/apply_fun_3.txt", "w") as f:
    f.write(f"{apply_fun_3}\n")

with open(f"{path}/list_row_wise_1.txt", "w") as f:
    f.write(f"{grades}\n")

with open(f"{path}/list_row_wise_2.txt", "w") as f:
    f.write(f"{row_wise_2}\n")
