from .dataset import df

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
