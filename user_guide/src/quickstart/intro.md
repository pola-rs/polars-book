# Getting started

## Installation

Installing and using `Polars` is just a simple `pip install`, `cargo add`, or `yarn add` away.

<div class="tabbed-blocks">

```python
# Installing for python
$ pip install polars
```

```rust,noplayground
// Installing into a Rust project
$ cargo add polars
```

```js
// Installing for Node
$ yarn add nodejs-polars
```

</div>

All binaries are pre-built for `Python` v3.6+.

## Quick start

Below we show a simple snippet that parses a CSV file, filters it, and finishes with a
groupby operation.  This example is presented in python only, as the "eager" API is not the preferred model in Rust.

```python
import polars as pl

df = pl.read_csv("https://j.mp/iriscsv")
print(df.filter(pl.col("sepal_length") > 5)
      .groupby("species", maintain_order=True)
      .agg(pl.all().sum())
)
```

The snippet above will output:

```text
shape: (3, 5)
┌────────────┬──────────────┬─────────────┬──────────────┬─────────────┐
│ species    ┆ sepal_length ┆ sepal_width ┆ petal_length ┆ petal_width │
│ ---        ┆ ---          ┆ ---         ┆ ---          ┆ ---         │
│ str        ┆ f64          ┆ f64         ┆ f64          ┆ f64         │
╞════════════╪══════════════╪═════════════╪══════════════╪═════════════╡
│ setosa     ┆ 116.9        ┆ 81.7        ┆ 33.2         ┆ 6.1         │
├╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌╌┤
│ versicolor ┆ 281.9        ┆ 131.8       ┆ 202.9        ┆ 63.3        │
├╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌╌┤
│ virginica  ┆ 324.5        ┆ 146.2       ┆ 273.1        ┆ 99.6        │
└────────────┴──────────────┴─────────────┴──────────────┴─────────────┘
```

As we can see, `Polars` pretty-prints the output object, including the column name and
datatype as headers.

## Lazy quick start

If we want to run this query in `lazy Polars` we'd write:

<div class="tabbed-blocks">

```python
import polars as pl

print(
    pl.read_csv("https://j.mp/iriscsv")
    .lazy()
    .filter(pl.col("sepal_length") > 5)
    .groupby("species", maintain_order=True)
    .agg(pl.all().sum())
    .collect()
)
```

```rust,noplayground
use color_eyre::{Result};
use std::io::Cursor;
use polars::prelude::*;
use reqwest::blocking::Client;

fn main() -> Result<()> { 
    let data: Vec<u8> = Client::new()
        .get("https://j.mp/iriscsv")
        .send()?
        .text()?
        .bytes()
        .collect();

    let df = CsvReader::new(Cursor::new(data))
        .has_header(true)
        .finish()?
        .lazy()
        .filter(col("sepal_length").gt(5))
        .groupby([col("species")])
        .agg([col("*").sum()])
        .collect()?;

    println!("{:?}", df);

    Ok(())
}
```

</div>

When the data is stored locally, we can also use `scan_csv` in Python, or `LazyCsvReader` in Rust to run the query in lazy polars.

### Note about Rust usage

Some functionality is not enabled by default. It must be added as an additional feature. This can be enabled by directly adding it to your `Cargo.toml`

```toml
[dependencies]
polars = { version = "0.24.3", features = ["lazy"] }
reqwest =  { version = "0.11.12", features = ["blocking"] }
color-eyre = "0.6"
```

## References

If you want to dive right into the `Python` API docs, check the [the reference docs](POLARS_PY_REF_GUIDE).  Alternatively, the `Rust` API docs are available on [docs.rs](https://docs.rs/polars/latest/polars/).

### Lazy API

The lazy API builds a query plan. Nothing is executed until you explicitly ask `Polars`
to execute the query (via `LazyFrame.collect()`, or `LazyFrame.fetch()`). This provides
`Polars` with the entire context of the query, allowing optimizations and choosing the
fastest algorithm given that context.

Going from eager to lazy is often as simple as starting your query with `.lazy()` and ending with `.collect()`.

So the eager snippet above would become:

<div class="tabbed-blocks">

```python
(
    df.lazy()
    .filter(pl.col("sepal_length") > 5)
    .groupby("species", maintain_order=True)
    .agg(pl.all().sum())
    .collect()
)
```

```rust,noplayground
let df = df
    .lazy()
    .filter(col("sepal_length").gt(5))
    .groupby([col("species")])
    .agg([col("*" ).sum()])
    .collect()?;
```

</div>
