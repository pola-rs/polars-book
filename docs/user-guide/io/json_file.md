# JSON files

## Read & Write

### JSON

Reading a JSON file should look familiar:


=== ":fontawesome-brands-python: Python"
    ``` python
    --8<-- "user-guide/python/io/json.py:read"
    ```


### Newline Delimited JSON

JSON objects that are delimited by newlines can be read into polars in a much more performant way than standard json.

=== ":fontawesome-brands-python: Python"
    ``` python
    --8<-- "user-guide/python/io/json.py:readnd"
    ```

## Write


=== ":fontawesome-brands-python: Python"
    ``` python
    --8<-- "user-guide/python/io/json.py:write"
    ```

## Scan

`Polars` allows you to _scan_ a JSON input **only for newline delimited json**. Scanning delays the actual parsing of the
file and instead returns a lazy computation holder called a `LazyFrame`.

=== ":fontawesome-brands-python: Python"
    ``` python
    --8<-- "user-guide/python/io/json.py:scan"
    ```

### Note about Rust usage

json functionality is not enabled by default. It must be added as an additional feature.
This can be enabled via `cargo add polars --features json` or by directly adding it to your `Cargo.toml`

```toml
[dependencies]
polars = { version = "0.24.3", features = ["json"] }
```

Additionally, scanning of json files requires the `lazy` feature

```toml
[dependencies]
polars = { version = "0.24.3", features = ["json", "lazy"] }
```