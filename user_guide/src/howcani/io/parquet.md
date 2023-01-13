# Parquet

Loading or writing [`Parquet` files](https://parquet.apache.org/) is lightning fast.
`Pandas` uses [`PyArrow`](https://arrow.apache.org/docs/python/) -`Python` bindings
exposed by `Arrow`- to load `Parquet` files into memory, but it has to copy that data into
`Pandas` memory. With `Polars` there is no extra cost due to
copying as we read `Parquet` directly into `Arrow` memory and _keep it there_.

## Read

<div class="tabbed-blocks">

```python
df = pl.read_parquet("path.parquet")
```

```rust,noplayground

let mut file = std::fs::File::open("path.parquet").unwrap();

let df = ParquetReader::new(&mut file).finish().unwrap();
```

</div>

## Write

<div class="tabbed-blocks">

```python
df = pl.DataFrame({"foo": [1, 2, 3], "bar": [None, "bak", "baz"]})
df.write_parquet("path.parquet")
```

```rust,noplayground
let mut df = df!(
    "foo" => &[1, 2, 3],
    "bar" => &[None, Some("bak"), Some("baz")],
)
.unwrap();

let mut file = std::fs::File::create("path.parquet").unwrap();
ParquetWriter::new(&mut file).finish(&mut df).unwrap();
```

</div>

## Scan

`Polars` allows you to _scan_ a `Parquet` input. Scanning delays the actual parsing of the
file and instead returns a lazy computation holder called a `LazyFrame`.

<div class="tabbed-blocks">

```python
df = pl.scan_parquet("path.parquet")
```

```rust,noplayground
use polars::prelude::*;

let args = ScanArgsParquet::default();
let df = LazyFrame::scan_parquet("./file.parquet",args).unwrap();
```

</div>

If you want to know why this is desirable,
you can read more about those `Polars` optimizations [here](../../optimizations/intro.md).

### Note about Rust usage

Parquet functionality is not enabled by default. It must be added as an additional feature.
This can be enabled via `cargo add polars --features parquet` or by directly adding it to your `Cargo.toml`

```toml
[dependencies]
polars = { version = "0.24.3", features = ["parquet"] }
```

Additionally, scanning of parquet files requires the `lazy` feature

```toml
[dependencies]
polars = { version = "0.24.3", features = ["parquet", "lazy"] }
```
