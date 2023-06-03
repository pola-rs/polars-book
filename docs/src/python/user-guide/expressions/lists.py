# --8<-- [start:setup]
import polars as pl

# --8<-- [end:setup]

# --8<-- [start:dataframe]
grades = pl.DataFrame(
    {
        "student": ["bas", "laura", "tim", "jenny"],
        "arithmetic": [10, 5, 6, 8],
        "biology": [4, 6, 2, 7],
        "geography": [8, 4, 9, 7],
    }
)
print(grades)
# --8<-- [end:dataframe]

# --8<-- [start:rank]
out = grades.select([pl.concat_list(pl.all().exclude("student")).alias("all_grades")])
print(out)
# --8<-- [end:rank]

# --8<-- [start:expression]
# the percentage rank expression
rank_pct = pl.element().rank(descending=True) / pl.col("*").count()

out = grades.with_columns(
    # create the list of homogeneous data
    pl.concat_list(pl.all().exclude("student")).alias("all_grades")
).select(
    [
        # select all columns except the intermediate list
        pl.all().exclude("all_grades"),
        # compute the rank by calling `list.eval`
        pl.col("all_grades").list.eval(rank_pct, parallel=True).alias("grades_rank"),
    ]
)
print(out)
# --8<-- [end:expression]
