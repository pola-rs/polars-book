from .guide_magic import my_datetime_list
import polars as pl


N = 1000

df = pl.DataFrame(
    {
        "rank": list(range(N)),
        "id": list(map(lambda x: str(x).zfill(5), range(N, 0, -1))),
        "date": my_datetime_list,
    }
)

pl.toggle_string_cache(True)
