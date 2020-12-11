from utils import peak_memory, gb_data_files, simple_bench
import pandas as pd


files = gb_data_files()


def groupby():
    df.groupby("str").first()


if __name__ == "__main__":
    with open("data/pandas_bench_gb.txt", "w") as fh:
        with open("data/pandas_gb_mem.txt", "w") as fh_mem:
            for fn in files:
                print(fn)
                df = pd.read_csv(fn)
                df = df.astype({"str": "str"})
                df = df[["str", "values"]]

                ms = simple_bench(groupby)
                print(ms)
                fh.write(f"{ms}\n")

                fh_mem.write(str(peak_memory()) + "\n")
