import datatable as dt
from utils import peak_memory, gb_data_files, simple_bench
import pypolars as pl
import pandas as pd


files = gb_data_files()


def read_dt():
    dt.fread(fn)


def read_polars():
    pl.read_csv(fn, n_threads=8, rechunk=False)


def read_pd():
    pd.read_csv(fn)


if __name__ == "__main__":
    with open("data/datatable_bench_csv_read.txt", "w") as fh:
        print("datatable")
        for fn in files:
            print(fn)
            ms = simple_bench(read_dt)
            print(ms)
            fh.write(f"{ms}\n")
        with open("data/pandas_bench_csv_read.txt", "w") as fh:
            print("polars")
            for fn in files:
                print(fn)
                ms = simple_bench(read_pd)
                print(ms)
                fh.write(f"{ms}\n")
        with open("data/polars_bench_csv_read.txt", "w") as fh:
            print("polars")
            for fn in files:
                print(fn)
                ms = simple_bench(read_polars)
                print(ms)
                fh.write(f"{ms}\n")
