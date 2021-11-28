from ..paths import OUTPUT_BASE_DIR, create_if_not_exists
from .add_column import out as add_df
from .casting import out as cast_df
from .dataset import df
from .drop_column import out as drop_df
from .rename_column import df as rename_df

path = create_if_not_exists(f"{OUTPUT_BASE_DIR}/df_manipulations")

with open(f"{path}/dataset.txt", "w") as f:
    f.write(f"{df}\n")

with open(f"{path}/rename_column.txt", "w") as f:
    f.write(f"{rename_df}\n")

with open(f"{path}/add_column.txt", "w") as f:
    f.write(f"{add_df}\n")

with open(f"{path}/casting.txt", "w") as f:
    f.write(f"{cast_df}\n")

with open(f"{path}/drop_column.txt", "w") as f:
    f.write(f"{drop_df}\n")

with open(f"{path}/drop_nulls.txt", "w") as f:
    f.write(f"{df.drop_nulls()}\n")

with open(f"{path}/fill_na.txt", "w") as f:
    f.write(f"{df.fill_null('forward')}\n")

with open(f"{path}/get_columns.txt", "w") as f:
    f.write(f"{df.columns}\n")

with open(f"{path}/null_count.txt", "w") as f:
    f.write(f"{df.null_count()}\n")

with open(f"{path}/sort_columns.txt", "w") as f:
    f.write(f"{df.sort('a', reverse=True)}\n")

with open(f"{path}/to_numpy.txt", "w") as f:
    f.write(f"{df.to_numpy()}\n")

with open(f"{path}/to_pandas.txt", "w") as f:
    f.write(f"{df.to_pandas()}\n")

with open(f"{path}/dtypes.txt", "w") as f:
    f.write(f"{df.dtypes}\n")
