import polars as pl

from ..paths import DATA_DIR

dataset = pl.read_csv(f"{DATA_DIR}/runescape.csv", has_headers=False, stop_after_n_rows=10)
