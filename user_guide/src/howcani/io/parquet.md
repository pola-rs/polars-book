# Parquet

Loading or writing [`Parquet` files](https://parquet.apache.org/) is as fast as can be.
`Pandas` uses [`PyArrow`](https://arrow.apache.org/docs/python/) -`Python` bindings
exposed by `Arrow`- to load `Parquet` files into memory but has to copy that data into
`Pandas` own memory. With `Polars` one does not have to pay the extra price due to
copying as we read `Parquet` directly into `Arrow memory` and *keep it there*.

## Read & write

```python
df = pl.read_parquet("path.parquet")
```

```python
df = pl.DataFrame({"foo": [1, 2, 3], "bar": [None, "bak", "baz"]})
df.to_parquet("path.parquet")
```

## Scan

`Polars` allows to *scan* a `Parquet` input. Scanning delays the actual parsing of the
file, and returns instead a lazy computation holder called a `LazyFrame`.

```python
df = pl.scan_parquet("path.parquet")
```

If you want to know why you would want this (and you do!)
[read about the optimizations](../../optimizations/intro.md) run under the hood of
`Polars`.
