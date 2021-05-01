# `Polars` User Guide

To build the benchmarks and `Python` code examples, `Graphviz`, `make`, `wget` as well as the `Python` packages listed in `requirements.txt` need to be present on the system.
To build the book, the `Rust`-based [`mdBook`](https://github.com/rust-lang/mdBook) executable should also be downloaded/compiled and accessible via the `PATH`.
To ease the few steps, a `Makefile` is provided; and a `Dockerfile` to build the complete environment:

```shell
$ docker build --build-arg uid=$UID -t polars-book .
$ docker run --entrypoint /bin/bash -it --rm -v `pwd`:/usr/src -p 8000:8000 --workdir /usr/src polars-book
```

should get you there.
(Note the `mdBook` executable is downloaded and *not* compiled to fasten the building of the image.)

### Status of the code snippets

| Example                                | `Python` |
|----------------------------------------|----------|
| CSV files                              | ✔        |
| Parquet files                          | ✔        |
| Interact with an AWS bucket            | ✔        |
| Interact with an Azure Blob Storage    | ✗        |
| Interact with a GCP Storage            | ✗        |
| Interact with a database               | ✗        |
| Process strings                        | ✔        |
| Process timestamps                     | ✔        |
| Process missing values                 | ✗        |
| Process nested values (explode)        | ✗        |
| Rename columns and other manipulations | ✗        |
| Column/row selection                   | ✗        |
| Filter                                 | ✗        |
| Group                                  | ✔        |
| Join                                   | ✗        |
| Sort                                   | ✗        |
| Pivot/melt                             | ✗        |
| Aggregate                              | ✔        |
| Conditionally apply                    | ✔        |
| Stacking                               | ✗        |
| Sampling                               | ✗        |
| `Arrow` interoperability               | ✔        |
| `NumPy` interoperability               | ✔        |
| Apply `NumPy` universal functions      | ✗        |
| Apply custom functions (UDFs)          | ✔        |
| Apply window functions                 | ✔        |
| Apply rolling-window functions         | ✗        |
| Group statistics                       | ✔        |
