# Parquet

Loading or writing [`Parquet` files](https://parquet.apache.org/) is lightning fast.
`Pandas` uses [`PyArrow`](https://arrow.apache.org/docs/python/) -`Python` bindings
exposed by `Arrow`- to load `Parquet` files into memory, but it has to copy that data into
`Pandas` memory. With `Polars` there is no extra cost due to
copying as we read `Parquet` directly into `Arrow` memory and _keep it there_.

## Read


=== ":fontawesome-brands-python: Python"
    ``` python
    --8<-- "user-guide/python/io/parquet.py:read"
    ```


## Write

=== ":fontawesome-brands-python: Python"
    ``` python
    --8<-- "user-guide/python/io/parquet.py:write"
    ```

## Scan

`Polars` allows you to _scan_ a `Parquet` input. Scanning delays the actual parsing of the
file and instead returns a lazy computation holder called a `LazyFrame`.

=== ":fontawesome-brands-python: Python"
    ``` python
    --8<-- "user-guide/python/io/parquet.py:scan"
    ```


If you want to know why this is desirable, you can read more about those `Polars` optimizations [here](../concepts/lazy-vs-eager.md).

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