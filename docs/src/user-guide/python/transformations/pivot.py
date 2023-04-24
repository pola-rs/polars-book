# --8<-- [start:setup]
import polars as pl

# --8<-- [end:setup]

# --8<-- [start:df]
df = pl.DataFrame(
    {
        "foo": ["A", "A", "B", "B", "C"],
        "N": [1, 2, 2, 4, 2],
        "bar": ["k", "l", "m", "n", "o"],
    }
)
# --8<-- [end:df]

# --8<-- [start:eager]

out = df.pivot(
    index="foo",
    columns="bar",
    values="N",
)
print(out)
# --8<-- [end:eager]

# --8<-- [end:lazy]
q = (
    df.lazy()
    .collect()
    .pivot(
        index="foo",
        columns="bar",
        values="N",
    )
    .lazy()
)
out = q.collect()
print(out)
# --8<-- [end:lazy]
