# Character-Separated Values

## Read & Write

Reading a CSV file should look familiar:

```python
df = pl.read_csv("path.csv")
```

CSV files come in many different flavors, so make sure to check the
[`read_csv()`](POLARS_PY_REF_GUIDE/api/polars.read_csv.html) API.

Writing to a CSV file can be done with the
[`write_csv()`](POLARS_PY_REF_GUIDE/api/polars.DataFrame.write_csv.html) method.

```python
df = pl.DataFrame({"foo": [1, 2, 3], "bar": [None, "bak", "baz"]})
df.write_csv("path.csv")
```

## Scan

`Polars` allows you to *scan* a CSV input. Scanning delays the actual parsing of the file
and instead returns a lazy computation holder called a `LazyFrame`.

```python
df = pl.scan_csv("path.csv")
```

If you want to know why this is desirable,
you can read more about those `Polars` optimizations [here](../../optimizations/intro.md).
