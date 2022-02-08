import polars as pl
import glob

queries = []
for file in glob.glob("my_many_files_*.csv"):
    q = pl.scan_csv(file).groupby("bar").agg([pl.count(), pl.sum("foo")])
    queries.append(q)

dataframes = pl.collect_all(queries)
