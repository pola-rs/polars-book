# JSON files

## Read & Write

### JSON

Reading a JSON file should look familiar:

{{code_block('user-guide/io/json-file','read',['read_json'])}}


### Newline Delimited JSON

JSON objects that are delimited by newlines can be read into polars in a much more performant way than standard json.

{{code_block('user-guide/io/json-file','readnd',['read_ndjson'])}}

## Write

{{code_block('user-guide/io/json-file','write',['write_json','write_ndjson'])}}


## Scan

`Polars` allows you to _scan_ a JSON input **only for newline delimited json**. Scanning delays the actual parsing of the
file and instead returns a lazy computation holder called a `LazyFrame`.

{{code_block('user-guide/io/json-file','scan',['scan_ndjson'])}}

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