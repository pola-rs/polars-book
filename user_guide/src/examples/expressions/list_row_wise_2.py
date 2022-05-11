import polars as pl

from .list_row_wise_1 import grades

out = grades.select([pl.concat_list(pl.all().exclude("student")).alias("all_grades")])
