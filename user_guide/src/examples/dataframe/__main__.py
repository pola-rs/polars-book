import polars as pl

from ..paths import OUTPUT_BASE_DIR, create_if_not_exists
from .dataset import df as dataset
from .add_col import df as dataset_column_added
from .replace import df as dataset_replaced
from .datatypes import df as dataset_new_datatypes
from .info import types, estimated_size
from .cat_join import color_ids
from .date_groupby import res as groupby_res


path = create_if_not_exists(f"{OUTPUT_BASE_DIR}/dataframe")

with open(f"{path}/df.txt", "w") as f:
    f.write(f"{dataset.sample()}\n")

with open(f"{path}/df_column_added.txt", "w") as f:
    f.write(f"{dataset_column_added.sample(3)}\n")

with open(f"{path}/df_replaced.txt", "w") as f:
    f.write(f"{dataset_replaced.tail()}\n")

with open(f"{path}/df_new_datatypes.txt", "w") as f:
    f.write(f"{dataset_new_datatypes.tail()}\n")

with open(f"{path}/df_info.txt", "w") as f:
    f.write(f"{(estimated_size, types)}\n")

with open(f"{path}/color_ids.txt", "w") as f:
    f.write(f"{color_ids.head()}\n")

with open(f"{path}/dates_groupby_res.txt", "w") as f:
    f.write(f"{groupby_res.head()}\n")

pl.toggle_string_cache(False)
