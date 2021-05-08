# `Polars` documentation

In this repo one can find the source of the [User Guide](https://pola-rs.github.io/polars-book/) of the [`Polars` DataFrame library](https://github.com/ritchie46/polars).

To build the benchmarks and `Python` code examples, `Graphviz`, `make`, `wget` as well as the `Python` packages listed in `requirements.txt` need to be present on the system.
To build the User Guide, the `Rust`-based [`mdBook`](https://github.com/rust-lang/mdBook) executable should also be downloaded/compiled and accessible (in the `PATH`).
To build the Reference Guide, a custom `mdBook` executable should also be downloaded from [here](https://github.com/ritchie46/mdBook/releases/download/api-0.0.1/mdbook) and made accessible as `mdbook2` in the `PATH`.
To ease the few steps, a `Makefile` is provided; and a `Dockerfile` to build the complete environment:

```shell
$ docker build --build-arg uid=$UID -t polars-guides .
$ docker run --entrypoint /bin/bash -it --rm -v `pwd`:/usr/src -p 8000:8000 --workdir /usr/src polars-guides
```

should get you there.
(Note the `mdBook` executable is downloaded and *not* compiled to fasten the building of the image.)

## User Guide

### Status of the code snippets

| Example                                | `Rust` | `Python` |
|----------------------------------------|--------|----------|
| CSV files                              | ✗      | ✔        |
| Parquet files                          | ✗      | ✔        |
| Interact with an AWS bucket            | ✗      | ✔        |
| Interact with an Azure Blob Storage    | ✗      | ✗        |
| Interact with a GCP Storage            | ✗      | ✗        |
| Interact with a database               | ✗      | ✗        |
| Process strings                        | ✗      | ✔        |
| Process timestamps                     | ✗      | ✔        |
| Process missing values                 | ✗      | ✗        |
| Process nested values (explode)        | ✗      | ✗        |
| Rename columns and other manipulations | ✗      | ✗        |
| Column/row selection                   | ✗      | ✗        |
| Filter                                 | ✗      | ✗        |
| Group                                  | ✗      | ✔        |
| Join                                   | ✗      | ✗        |
| Sort                                   | ✗      | ✗        |
| Pivot/melt                             | ✗      | ✗        |
| Aggregate                              | ✗      | ✔        |
| Conditionally apply                    | ✗      | ✔        |
| Horizontal fold                        | ✗      | ✗        |
| Stacking                               | ✗      | ✗        |
| Sampling                               | ✗      | ✗        |
| `Arrow` interoperability               | ✗      | ✔        |
| `NumPy` interoperability               | ✗      | ✔        |
| Apply `NumPy` universal functions      | ✗      | ✗        |
| Apply custom functions (UDFs)          | ✗      | ✔        |
| Apply window functions                 | ✗      | ✔        |
| Apply rolling-window functions         | ✗      | ✗        |
| Group statistics                       | ✗      | ✔        |

## Reference Guides

At this point in time, only `Python` bindings are available for `Polars`.

> We are actively looking for `Node` experts to implement `JavaScript` bindings!

The content of the Reference Guides is generated directly from the source code.
In this repo one can find the scripts used to generate the `Markdown` content later rendered by `mdBook` (a custom version thereof).
