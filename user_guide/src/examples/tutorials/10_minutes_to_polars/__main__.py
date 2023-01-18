from ...paths import OUTPUT_BASE_DIR, create_if_not_exists
from .creating_a_dataframe import df
from .square_brackets import square_brackets_df
from .select import select_df
from .select_transform import select_transform_df
from .select_chain import select_chain_df
from .with_columns import with_columns_df
from .filter_dataframe import filtered_df
from .filter_dataframe_and import joint_filtered_df
from .groupby_dataframe import grouped_df
from .groupby_dataframe_lazy import lazy_grouped_df, lazy_grouped_plan
from .filter_dataframe_lazy import lazy_filter_grouped_df
from .evaluate_dataframe_lazy import evaluate_grouped_df, fetch_grouped_df, stream_grouped_df

path = create_if_not_exists(f"{OUTPUT_BASE_DIR}/tutorials/10-minutes-to-polars")

variable_filename_tuples = [
    (df, "df_head"),
    (square_brackets_df, "square_brackets_df"),
    (select_df, "select_df"),
    (select_transform_df, "select_transform_df"),
    (select_chain_df, "select_chain_df"),
    (with_columns_df, "with_columns_df"),
    (filtered_df, "filtered_df"),
    (joint_filtered_df, "joint_filtered_df"),
    (grouped_df, "grouped_df"),
    (lazy_grouped_df, "lazy_grouped_df"),
    (lazy_grouped_plan, "lazy_grouped_plan"),
    (lazy_filter_grouped_df, "lazy_filter_grouped_df"),
    (evaluate_grouped_df, "evaluate_grouped_df"),
    (fetch_grouped_df, "fetch_grouped_df"),
    (stream_grouped_df, "stream_grouped_df"),
]

for variable, filename in variable_filename_tuples:
    with open(f"{path}/{filename}.txt", "w") as f:
        f.write(f"{variable}\n")
