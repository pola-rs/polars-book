from ..paths import OUTPUT_BASE_DIR, create_if_not_exists
from .combining_data_examples import (
    df_v1,
    df_v2,
    df_vertical_concat,
    df_h1,
    df_h2,
    df_horizontal_concat,
    df_d1,
    df_d2,
    df_diagonal_concat,
    df_cars,
    df_repairs,
    df_inner_join,
    df_semi_join,
    df_anti_join,
    df_trades,
    df_quotes,
    df_asof_join,
    df_asof_tolerance_join,
)

path = create_if_not_exists(f"{OUTPUT_BASE_DIR}/combining_data")

variable_filename_tuples = [
    (df_v1, "df_v1"),
    (df_v2, "df_v2"),
    (df_vertical_concat, "df_vertical_concat"),
    (df_h1, "df_h1"),
    (df_h2, "df_h2"),
    (df_horizontal_concat, "df_horizontal_concat"),
    (df_d1, "df_d1"),
    (df_d2, "df_d2"),
    (df_diagonal_concat, "df_diagonal_concat"),
    (df_cars, "df_cars"),
    (df_repairs, "df_repairs"),
    (df_inner_join, "df_inner_join"),
    (df_semi_join, "df_semi_join"),
    (df_anti_join, "df_anti_join"),
    (df_trades, "df_trades"),
    (df_quotes, "df_quotes"),
    (df_asof_join, "df_asof_join"),
    (df_asof_tolerance_join, "df_asof_tolerance_join"),
]

for variable, filename in variable_filename_tuples:
    with open(f"{path}/{filename}.txt", "w") as f:
        f.write(f"{variable}\n")
