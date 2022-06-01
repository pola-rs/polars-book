from ..paths import OUTPUT_BASE_DIR, create_if_not_exists
from .days_month import out as days_month
from .dynamic_ds import df as dyn_df
from .dynamic_groupby import out as dyn_gb
from .parsing_dates import df as parse_dates_df, filtered_df, filtered_range_df, annual_average_df, df_with_year
from .cast_date_to_string import df as cast_date_to_string_df
from .resampling_example import df as resample_df, out1, out2

path = create_if_not_exists(f"{OUTPUT_BASE_DIR}/time_series")

with open(f"{path}/days_month.txt", "w") as f:
    f.write(f"{days_month}\n")

with open(f"{path}/dyn_df.txt", "w") as f:
    f.write(f"{dyn_df}\n")

with open(f"{path}/dyn_gb.txt", "w") as f:
    f.write(f"{dyn_gb}\n")

with open(f"{path}/parse_dates_example_df.txt", "w") as f:
    f.write(f"{parse_dates_df}\n")

with open(f"{path}/cast_string_to_date_example_df.txt", "w") as f:
    f.write(f"{cast_date_to_string_df}\n")

with open(f"{path}/parse_dates_filtered_df.txt", "w") as f:
    f.write(f"{filtered_df}\n")

with open(f"{path}/parse_dates_filtered_range_df.txt", "w") as f:
    f.write(f"{filtered_range_df}\n")

with open(f"{path}/parse_dates_annual_average_df.txt", "w") as f:
    f.write(f"{annual_average_df}\n")

with open(f"{path}/parse_dates_with_year.txt", "w") as f:
    f.write(f"{df_with_year}\n")


with open(f"{path}/resample_example_df.txt", "w") as f:
    f.write(f"{resample_df}\n")

with open(f"{path}/resample_upsample_output.txt", "w") as f:
    f.write(f"{out1}\n")

with open(f"{path}/resample_upsample_interpolation.txt", "w") as f:
    f.write(f"{out2}\n")
