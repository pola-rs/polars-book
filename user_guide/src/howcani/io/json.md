# JSON files

## Read & Write

### JSON

Reading a JSON file should look familiar:

<div class="tabbed-blocks">

```python
df = pl.read_json("path.json")
```

```rust,noplayground
use polars::prelude::*;

let mut file = std::fs::File::open("path.json").unwrap();
let df = JsonReader::new(&mut file).finish().unwrap();
```
</div>


### Newline Delimited JSON
JSON objects that are delimited by newlines can be read into polars in a much more performant way than standard json.

<div class="tabbed-blocks">

```python
df = pl.read_ndjson("path.json")
```

```rust,noplayground
use polars::prelude::*;

let mut file = std::fs::File::open("path.json").unwrap();
let df = JsonLineReader::new(&mut file).finish().unwrap();
```
</div>

## Write

<div class="tabbed-blocks">

```python
df = pl.DataFrame({"foo": [1, 2, 3], "bar": [None, "bak", "baz"]})
# json
df.write_json("path.json")
# ndjson
df.write_ndjson("path.json")
```

```rust,noplayground
use polars::prelude::*;

let mut df = df!(
    "foo" => [1, 2, 3],
    "bar" => [None, Some("bak"), Some("baz")],
)
.unwrap();

let mut file = std::fs::File::create("path.csv").unwrap();

// json
JsonWriter::new(&mut file)
    .with_json_format(JsonFormat::Json)
    .finish(&mut df)
    .unwrap();

// ndjson
JsonWriter::new(&mut file)
    .with_json_format(JsonFormat::JsonLines)
    .finish(&mut df)
    .unwrap();
```

</div>

## Scan

`Polars` allows you to *scan* a JSON input **only for newline delimited json**. Scanning delays the actual parsing of the
file and instead returns a lazy computation holder called a `LazyFrame`.

<div class="tabbed-blocks">


```python
df = pl.scan_ndjson("path.json")
```

```rust,noplayground
use polars::prelude::*;

let df = LazyJsonLineReader::new("path.json".to_string()).finish().unwrap();
```
</div>


### Note about Rust usage

Parquet functionality is not enabled by default. It must be added as an additional feature.
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
