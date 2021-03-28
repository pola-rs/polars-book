# File IO

Polars support different file types and has its parsers are amongst the fastest there are. For instance,
it's faster to load a CSV via polars to pandas, than directly from pandas. 
Just do `pl.read_CSV("path.txt", rechunk=False).to_pandas()` and you're off.

## CSV files
So with that fun fact out of the way, loading a CSV file should be familiar:

### Read CSV
```python
import polars as pl

df = pl.read_csv("path.csv")
```

CSV files come in many different flavors, so make sure to check the 
[read_csv API](POLARS_API_LINK/functions.html#polars.functions.read_csv).

Writing to a CSV file can be done with [to_csv](POLARS_API_LINK/frame.html#polars.frame.DataFrame.to_csv).

### Write CSV
```python
import polars as pl
df = pl.DataFrame({
    "foo": [1, 2, 3],
    "bar": [None, "egg", "spam"]
})

df.to_csv("path.csv")
```

## Parquet files
Loading and writing parquet files are also as fast as can be. Pandas uses pyarrow to load parquet files into arrow memory
and then has to copy that memory into pandas acceptable memory. In polars we don't have to pay that copy price, because
we read parquet directly into arrow memory and we keep it there.

### Read Parquet
```python
import polars as pl

df = pl.read_parquet("path.csv")
```

### Write Parquet
```python
import polars as pl
df = pl.DataFrame({
    "foo": [1, 2, 3],
    "bar": [None, "egg", "spam"]
})

df.to_parquet("path.csv")
```

## Scanning files

You can also scan a csv, and parquet files. Scanning delays the actual parsing of the files and returns a lazy computation
holder, called a `LazyFrame`. If you want to know why you'd want this (and you do!) [read the lazy introduction](../lazy_polars/intro.md)

```python
import polars as pl

# start a lazy query from a csv file.
lf = pl.scan_csv("path.csv")


# start a lazy query from a parquet file.
lf = pl.scan_parquet("path.parquet")
```

