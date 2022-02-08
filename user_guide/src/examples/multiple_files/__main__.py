from ..paths import OUTPUT_BASE_DIR, create_if_not_exists

path = create_if_not_exists(f"{OUTPUT_BASE_DIR}/multiple_files")
import os

# make sure that all scripts write to this path
os.chdir(path)

# import for state effect
from .dataset import df as _

from .single_df import df as df_single
from .single_df_plan import pl as _
from .multiple_queries import dataframes

with open(f"single_df.txt", "w") as f:
    f.write(f"{df_single}\n")

with open(f"dataframes.txt", "w") as f:
    f.write(f"{dataframes}\n")
