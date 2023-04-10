import polars as pl

from .dynamic_ds import df

out = df.groupby_dynamic("time", every="1h", closed="both", by="groups", include_boundaries=True,).agg(
    [
        pl.count(),
    ]
)
