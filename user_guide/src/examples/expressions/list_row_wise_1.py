import polars as pl

grades = pl.DataFrame(
    {
        "student": ["bas", "laura", "tim", "jenny"],
        "arithmetic": [10, 5, 6, 8],
        "biology": [4, 6, 2, 7],
        "geography": [8, 4, 9, 7],
    }
)
