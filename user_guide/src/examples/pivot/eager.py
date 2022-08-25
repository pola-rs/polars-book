from .dataset import df

out = df.pivot(
    index="foo",
    columns="bar",
    values="N",
)
