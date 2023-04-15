---
hide:
  - navigation
---
# Polars

![logo](https://raw.githubusercontent.com/pola-rs/polars-static/master/logos/polars_github_logo_rect_dark_name.svg)

<h1 style="text-align:center">Blazingly Fast DataFrame Library </h1>
<div align="center">
  <a href="https://docs.rs/polars/latest/polars/">
    <img src="https://docs.rs/polars/badge.svg" alt="rust docs"/>
  </a>
  <a href="https://github.com/pola-rs/polars/actions">
    <img src="https://github.com/pola-rs/polars/workflows/Build%20and%20test/badge.svg" alt="Build and test"/>
  </a>
  <a href="https://crates.io/crates/polars">
    <img src="https://img.shields.io/crates/v/polars.svg"/>
  </a>
  <a href="https://pypi.org/project/polars/">
    <img src="https://img.shields.io/pypi/v/polars.svg" alt="PyPi Latest Release"/>
  </a>
  <a href="https://www.npmjs.com/package/nodejs-polars">
    <img src="https://img.shields.io/npm/v/nodejs-polars.svg" alt="NPM Latest Release"/>
  </a>
  <a href="https://doi.org/10.5281/zenodo.7697217">
    <img src="https://zenodo.org/badge/DOI/10.5281/zenodo.7697217.svg" alt="DOI Latest Release"/>
  </a>
</div>

Polars is a highly performant DataFrame library for manipulating structured data. The core is written in Rust, but the library is available in Python, Rust & NodeJS. Its key features are:


- **Fast**: Polars is written from the ground up, designed close to the machine and without external dependencies. 
- **I/O**: First class support for all common data storage layers: local, cloud storage & databases. 
- **Easy to use**: Write your queries the way they were intended. Polars, internally, will determine the most efficient way to execute using its query optimizer.
- **Out of Core**: Polars supports out of core data transformation with its streaming API. Allowing you to process your results without requiring all your data to be in memory at the same time
- **Parallel**: Polars fully utilises the power of your machine by dividing the workload among the available CPU cores without any additional configuration. 
- **Vectorized Query Engine**: Polars uses [Apache Arrow](https://arrow.apache.org/), a columnar data format, to process your queries in a vectorized manner. It uses [SIMD](https://en.wikipedia.org/wiki/Single_instruction,_multiple_data) to optimize CPU usage.

## About this guide

The `Polars` user guide is intended to live alongside the API documentation. Its purpose is to explain (new) users how to use `Polars` and to provide meaningfull examples. The guide is split into two parts:

- [Getting Started](../docs/getting-started/intro.md): A 10 minute helicopter view of the library and its primary function.
- [User Guide](../docs/user-guide/index.md): A detailed explanation of how the library is setup and how to use it most effectively. 

If you are looking for details on a specific level / object, it is probably best to go the API documentation: [Python](https://pola-rs.github.io/polars/py-polars/html/reference/index.html) | [NodeJS](https://pola-rs.github.io/polars/polars/index.html) | [Rust](https://pola-rs.github.io/polars/polars/index.html).

## Performance :rocket: :rocket:

`Polars` is very fast, and in fact is one of the best performing solutions available.
See the results in h2oai's [db-benchmark](https://h2oai.github.io/db-benchmark/). 

`Polars` [TPCH Benchmark results](https://www.pola.rs/benchmarks.html) are now available on the official website.


## Example

=== ":fontawesome-brands-python: Python"
    ``` python
    --8<-- "home/python/example.py:example"
    ```

=== ":fontawesome-brands-rust: Rust"

    ``` rust
    --8<-- "home/rust/example.rs:example"
    ```
=== ":fontawesome-brands-node-js: NodeJS"

    ``` javaScript
    --8<-- "home/node/example.js:example"
    ```


## Goals

The goal of `Polars` is to provide a lightning fast `DataFrame` library that:

- Utilizes all available cores on your machine.
- Optimizes queries to reduce unneeded work/memory allocations.
- Handles datasets much larger than your available RAM.
- Has an API that is consistent and predictable.
- Has a strict schema (data-types should be known before running the query).

Polars is written in Rust which gives it C/C++ performance and allows it to fully control performance critical parts
in a query engine.

As such `Polars` goes to great lengths to:

- Reduce redundant copies.
- Traverse memory cache efficiently.
- Minimize contention in parallelism.
- Process data in chunks.
- Reuse memory allocations.

## Sponsors

[<img src="https://raw.githubusercontent.com/pola-rs/polars-static/master/sponsors/xomnia.png" style="height:50px"/>](https://www.xomnia.com/) &emsp; [<img src="https://www.jetbrains.com/company/brand/img/jetbrains_logo.png" style="height:50px"; />](https://www.jetbrains.com)

## Community

`Polars` has a very active community with frequent releases (approximately weekly). Below are the top 50 contributors to the project sorted by number of contributions: 

--8<-- "docs/people.md"


## Contribute 

Thanks for taking the time to contribute! We appreciate all contributions, from reporting bugs to implementing new features. If you're unclear on how to proceed read our [contribution guide](https://github.com/pola-rs/polars/blob/main/CONTRIBUTING.md) or contact us on [discord](https://discord.com/invite/4UfP5cfBE7).


## License

This project is licensed under the terms of the [MIT license](https://opensource.org/license/mit/).