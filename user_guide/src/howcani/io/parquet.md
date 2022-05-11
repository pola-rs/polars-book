# Parquet

Loading or writing [`Parquet` files](https://parquet.apache.org/) is lightning fast.
`Pandas` uses [`PyArrow`](https://arrow.apache.org/docs/python/) -`Python` bindings
exposed by `Arrow`- to load `Parquet` files into memory, but it has to copy that data into
`Pandas` memory. With `Polars` there is no extra cost due to
copying as we read `Parquet` directly into `Arrow` memory and *keep it there*.

## Read & write

```python
df = pl.read_parquet("path.parquet")
```

```python
df = pl.DataFrame({"foo": [1, 2, 3], "bar": [None, "bak", "baz"]})
df.write_parquet("path.parquet")
```

## Scan

`Polars` allows you to *scan* a `Parquet` input. Scanning delays the actual parsing of the
file and instead returns a lazy computation holder called a `LazyFrame`.

```python
df = pl.scan_parquet("path.parquet")
```

If you want to know why this is desirable,
you can read more about those `Polars` optimizations [here](../../optimizations/intro.md).
