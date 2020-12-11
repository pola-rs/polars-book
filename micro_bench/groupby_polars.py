from utils import peak_memory, gb_data_files, simple_bench
import pypolars as pl


files = gb_data_files()


def groupby():
    df.groupby("str").select("values").first()


if __name__ == "__main__":
    with open("data/polars_bench_gb.txt", "w") as fh:
        with open("data/polars_gb_mem.txt", "w") as fh_mem:
            for fn in files:
                print(fn)
                df = pl.read_csv(fn)
                df["str"] = df["str"].cast(str)
                ms = simple_bench(groupby)
                print(ms)
                fh.write(f"{ms}\n")

                fh_mem.write(str(peak_memory()) + "\n")
