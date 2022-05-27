from ..paths import OUTPUT_BASE_DIR, create_if_not_exists
from .missing_types import df, nullCountDf, isNullSeries, dfNaN
from .fill_strategies import df as fillDf, fillLiteral, fillForward, fillMedian, fillInterpolation

path = create_if_not_exists(f"{OUTPUT_BASE_DIR}/missing_data")

variable_filename_tuples = [
    (df, "none_missing_value_df"),
    (nullCountDf, "null_count_df"),
    (isNullSeries, "isnull_series"),
    (dfNaN, "nan_missing_value_df"),
    (fillDf, "fill_strategies_df"),
    (fillLiteral, "fill_strategies_literal_df"),
    (fillForward, "fill_strategies_forward_df"),
    (fillMedian, "fill_strategies_median_df"),
    (fillInterpolation, "fill_strategies_interpolate_df"),
]

for variable, filename in variable_filename_tuples:
    with open(f"{path}/{filename}.txt", "w") as f:
        f.write(f"{variable}\n")
