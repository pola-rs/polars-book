from ..paths import OUTPUT_BASE_DIR, create_if_not_exists
from .days_month import out as days_month
from .dynamic_ds import df as dyn_df
from .dynamic_groupby import out as dyn_gb
from .parsing_dates import (
    df as parse_dates_df,
    filtered_df,
    filtered_range_df,
    annual_average_df,
    df_with_year,
    negative_dates_filtered_df,
)
from .cast_date_to_string import df as cast_date_to_string_df
from .resampling_example import df as resample_df, out1, out2
from .time_zones import (
    with_offset_parsed,
    tz_naive,
    tz_aware,
    out_1 as tz_aware_from_utc,
    out_2 as timezone_set_on_tz_naive,
    out_3 as tz_aware_to_different_timezone,
    out_4 as tz_aware_with_changed_timezone,
    out_5 as tz_aware_to_naive,
)

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

with open(f"{path}/negative_dates_filtered_df.txt", "w") as f:
    f.write(f"{negative_dates_filtered_df}\n")

with open(f"{path}/resample_example_df.txt", "w") as f:
    f.write(f"{resample_df}\n")

with open(f"{path}/resample_upsample_output.txt", "w") as f:
    f.write(f"{out1}\n")

with open(f"{path}/resample_upsample_interpolation.txt", "w") as f:
    f.write(f"{out2}\n")

with open(f"{path}/with_offset_parsed.txt", "w") as f:
    f.write(f"{with_offset_parsed}\n")

with open(f"{path}/tz_naive.txt", "w") as f:
    f.write(f"{tz_naive}\n")

with open(f"{path}/tz_aware.txt", "w") as f:
    f.write(f"{tz_aware}\n")

with open(f"{path}/tz_aware_from_utc.txt", "w") as f:
    f.write(f"{tz_aware_from_utc}\n")

with open(f"{path}/timezone_set_on_tz_naive.txt", "w") as f:
    f.write(f"{timezone_set_on_tz_naive}\n")

with open(f"{path}/tz_aware_to_different_timezone.txt", "w") as f:
    f.write(f"{tz_aware_to_different_timezone}\n")

with open(f"{path}/tz_aware_with_changed_timezone.txt", "w") as f:
    f.write(f"{tz_aware_with_changed_timezone}\n")

with open(f"{path}/tz_aware_to_naive.txt", "w") as f:
    f.write(f"{tz_aware_to_naive}\n")
