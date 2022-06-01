from ..paths import OUTPUT_BASE_DIR, create_if_not_exists
from .missing_types import df, null_count_df, is_null_series, nan_df
from .fill_strategies import (
    df as fill_df,
    fill_literal_df,
    fill_forward_df,
    fill_median_df,
    fill_interpolation_df,
    mean_nan_df,
)

path = create_if_not_exists(f"{OUTPUT_BASE_DIR}/missing_data")

variable_filename_tuples = [
    (df, "none_missing_value_df"),
    (null_count_df, "null_count_df"),
    (is_null_series, "isnull_series"),
    (nan_df, "nan_missing_value_df"),
    (fill_df, "fill_strategies_df"),
    (fill_literal_df, "fill_strategies_literal_df"),
    (fill_forward_df, "fill_strategies_forward_df"),
    (fill_median_df, "fill_strategies_median_df"),
    (fill_interpolation_df, "fill_strategies_interpolate_df"),
    (mean_nan_df, "fill_strategies_mean_df"),
]

for variable, filename in variable_filename_tuples:
    with open(f"{path}/{filename}.txt", "w") as f:
        f.write(f"{variable}\n")
