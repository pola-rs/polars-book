import polars as pl
"""
# --8<-- [start:plan]
q1 = (
    pl.scan_csv(f"docs/src/lazy/reddit.csv")
    .with_columns(pl.col("name").str.to_uppercase())
    .filter(pl.col("comment_karma") > 0)
)

q1.show_graph(optimized=False)
# --8<-- [end:plan]

# --8<-- [start:describe]
q1.describe_plan()
# --8<-- [end:describe]

# --8<-- [start:show]
q1.show_graph()
# --8<-- [end:show]

# --8<-- [start:optimized]
q1.describe_optimized_plan()
# --8<-- [end:optimized]
"""