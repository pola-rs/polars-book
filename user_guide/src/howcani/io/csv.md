# Character-Separated Values

## Read & Write

Reading a CSV file should look familiar:

```python
df = pl.read_csv("path.csv")
```

CSV files come in many different flavors, so make sure to check the
[`read_csv()`](POLARS_PY_REF_GUIDE/functions.html#polars.functions.read_csv) API.

Writing to a CSV file can be done with the
[`to_csv()`](POLARS_PY_REF_GUIDE/frame.html#polars.frame.DataFrame.to_csv) method.

```python
df = pl.DataFrame({"foo": [1, 2, 3], "bar": [None, "bak", "baz"]})
df.to_csv("path.csv")
```

## Scan

`Polars` allows to *scan* a CSV input. Scanning delays the actual parsing of the file,
and returns instead a lazy computation holder called a `LazyFrame`.

```python
df = pl.scan_csv("path.csv")
```

If you want to know why you would want this (and you do!)
[read about the optimizations](../../optimizations/intro.md) run under the hood of
`Polars`.
