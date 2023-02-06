from ..paths import OUTPUT_BASE_DIR, create_if_not_exists
from .vertical_concat_example import df_v1, df_v2, df_vertical_concat
from .horizontal_concat_example import df_h1, df_h2, df_horizontal_concat
from .diagonal_concat_example import df_d1, df_d2, df_diagonal_concat
from .inner_join_example import df_customers, df_orders, df_inner_customer_join
from .left_join_example import df_left_join
from .outer_join_example import df_outer_join
from .cross_join_example import df_colors, df_sizes, df_cross_join
from .semi_join_example import df_cars, df_repairs, df_inner_join, df_semi_join, df_anti_join
from .asof_join_example import df_trades, df_quotes, df_asof_join, df_asof_tolerance_join


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
    (df_customers, "df_customers"),
    (df_orders, "df_orders"),
    (df_inner_customer_join, "df_inner_customer_join"),
    (df_left_join, "df_left_join"),
    (df_outer_join, "df_outer_join"),
    (df_colors, "df_colors"),
    (df_sizes, "df_sizes"),
    (df_cross_join, "df_cross_join"),
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
