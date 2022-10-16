# Character-Separated Values

## Read & Write

Reading a CSV file should look familiar:

<div class="tabbed-blocks">

```python
df = pl.read_csv("path.csv")
```

```rust,noplayground
use polars::prelude::*;

let df = CsvReader::from_path("path.csv").unwrap().finish().unwrap();
```
</div>

CSV files come in many different flavors, so make sure to check the
[`read_csv()`](POLARS_PY_REF_GUIDE/api/polars.read_csv.html) API.

Writing to a CSV file can be done with the
[`write_csv()`](POLARS_PY_REF_GUIDE/api/polars.DataFrame.write_csv.html) method.

<div class="tabbed-blocks">

```python
df = pl.DataFrame({"foo": [1, 2, 3], "bar": [None, "bak", "baz"]})
df.write_csv("path.csv")
```

```rust,noplayground
use polars::prelude::*;

let mut df = df!(
    "foo" => [1, 2, 3],
    "bar" => [None, Some("bak"), Some("baz")],
)
.unwrap();

let mut file = std::fs::File::create("path.csv").unwrap();
CsvWriter::new(&mut file).finish(&mut df).unwrap();
```

</div>

## Scan

`Polars` allows you to *scan* a CSV input. Scanning delays the actual parsing of the
file and instead returns a lazy computation holder called a `LazyFrame`.

<div class="tabbed-blocks">


```python
df = pl.scan_csv("path.csv")
```

```rust,noplayground
use polars::prelude::*;

let df = LazyCsvReader::new("./test.csv").finish().unwrap();
```
</div>

If you want to know why this is desirable, you can read more about those `Polars`
optimizations [here](../../optimizations/intro.md).

The following video shows how to efficiently load CSV files with Polars and how the built-in query optimization makes this much faster.

<iframe width="560" height="315" src="https://www.youtube.com/embed/nGritAo-71o" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
