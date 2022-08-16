from ..paths import OUTPUT_BASE_DIR, create_if_not_exists
from .indexing_selecting_examples import (
    df,
    expression_df,
    filter_df,
    multi_filter_df,
    single_select_df,
    list_select_df,
    condition_select_df,
    dtype_select_df,
)
from .lazy_select_data import lazy_filter_df, lazy_select_df

path = create_if_not_exists(f"{OUTPUT_BASE_DIR}/selecting_data")

variable_filename_tuples = [
    (df, "simple_df"),
    (expression_df, "expression_df"),
    (filter_df, "filter_df"),
    (multi_filter_df, "multi_filter_df"),
    (single_select_df, "single_select_df"),
    (list_select_df, "list_select_df"),
    (condition_select_df, "condition_select_df"),
    (dtype_select_df, "dtype_select_df"),
    (lazy_filter_df, "lazy_filter_df"),
    (lazy_select_df, "lazy_select_df"),
]

for variable, filename in variable_filename_tuples:
    with open(f"{path}/{filename}.txt", "w") as f:
        f.write(f"{variable}\n")
