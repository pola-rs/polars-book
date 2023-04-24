<div style="margin: 30px auto; background-color: white; border-radius: 50%; width: 200px; height: 200px;"><img src="https://raw.githubusercontent.com/pola-rs/polars-static/master/logos/polars-logo-dark.svg" alt="Polars logo" style="width: 168px; height: 168px; padding: 10px 20px;"></div>

# Introduction

This book is an introduction to the
[`Polars` DataFrame library](https://github.com/pola-rs/polars). Its goal is to
introduce you to `Polars` by going through examples and comparing it to other
solutions. Some design choices are introduced here. The guide will also introduce you to
optimal usage of `Polars`.

Even though `Polars` is completely written in [`Rust`](https://www.rust-lang.org/) (no
runtime overhead!) and uses [`Arrow`](https://arrow.apache.org/) -- the
[native arrow2 `Rust` implementation](https://github.com/jorgecarleitao/arrow2) -- as its foundation, the
examples presented in this guide will be mostly using its higher-level language
bindings. Higher-level bindings only serve as a thin wrapper for functionality implemented in the core library.

For [`Pandas`](https://pandas.pydata.org/) users, our
[Python package](https://pypi.org/project/polars/) will offer the easiest way to get started with
`Polars`.

## Goals and non-goals

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

Polars also has control over IO, allowing it to save redundant copies and to push down projections and predicates to
the scan level.

Unlike tools such as dask -- which tries to parallelize existing single-threaded libraries
like `NumPy` and `Pandas` --`Polars` is written from the ground up, designed for parallelization of queries on `DataFrame`s.

`Polars` is lazy and semi-lazy. It allows you to do most of your work eagerly, similar to `Pandas`, but
it also provides a powerful expression syntax that will be optimized and executed on within the query engine.

In lazy `Polars` we are able to do query optimization on the entire query, further improving performance and memory pressure.

`Polars` keeps track of your query in a *logical plan*. This
plan is optimized and reordered before running it. When a result is requested, `Polars`
distributes the available work to different *executors* that use the algorithms available
in the eager API to produce a result. Because the whole query context is known to
the optimizer and executors of the logical plan, processes dependent on separate data
sources can be parallelized on the fly.

### Performance 🚀🚀

`Polars` is very fast, and in fact is one of the best performing solutions available.
See the results in h2oai's db-benchmark. The image below shows the biggest datasets yielding a result.

![](https://www.ritchievink.com/img/post-35-polars-0.15/db-benchmark.png)

`Polars` [TPCH Benchmark results](https://www.pola.rs/benchmarks.html) are now available on the official website.

### Current status

Below a concise list of the features allowing `Polars` to meet its goals:

- [Copy-on-write](https://en.wikipedia.org/wiki/Copy-on-write) (COW) semantics
  - "Free" clones
  - Cheap appends
- Appending without clones
- Column oriented data storage
  - No block manager (i.e. predictable performance)
- Missing values indicated with bitmask
  - NaN are different from missing
  - Bitmask optimizations
- Efficient algorithms
- Very fast IO
  - Its csv and parquet readers are among the fastest in existence
- Out of Core
  - Many queries can be executed completely out of core
    (meaning that we can process datasets that are larger than RAM)
  - Arrow/IPC files can be memory mapped (this is the strategy vaex uses)
- [Query optimizations](optimizations/lazy/intro.md)
  - Predicate pushdown
    - Filtering at scan level
  - Projection pushdown
    - Projection at scan level
  - Aggregate pushdown
    - Aggregations at scan level
  - Simplify expressions
  - Scan sharing
  - Common subplan elimination
  - Parallel execution of physical plan
  - Cardinality based groupby dispatch
    - Different groupby strategies based on data cardinality
- SIMD vectorization
- [`NumPy` universal functions](https://numpy.org/doc/stable/reference/ufuncs.html)

### Comparison with other tools

These are some tools that share similar functionality to what polars does.

- Pandas

  - A very versatile tool for small data. Read [10 things I hate about pandas](https://wesmckinney.com/blog/apache-arrow-pandas-internals/)
    written by the author himself. Polars has solved all those 10 things.
    Polars is a versatile tool for small and large data with a more predictable API, less ambiguous and stricter API.

- Pandas the API

  - The API of pandas was designed for in memory data. This makes it a poor fit for performant analysis on large data
    (read anything that does not fit into RAM). Any tool that tries to distribute that API will likely have a
    suboptimal query plan compared to plans that follow from a declarative API like SQL or polars' API.

- Dask

  - Parallelizes existing single-threaded libraries like `NumPy` and `Pandas`. As a consumer of those libraries Dask
    therefore has less control over low level performance and semantics.
    Those libraries are treated like a black box.
    On a single machine the parallelization effort can also be seriously stalled by pandas strings.
    Pandas strings, by default, are stored as python objects in
    numpy arrays meaning that any operation on them is GIL bound and therefore single threaded. This can be circumvented
    by multi-processing but has a non-trivial cost.

- Modin

  - Similar to Dask

- Vaex

  - Vaexs method of out-of-core analysis is memory mapping files. This works until it doesn't. For instance parquet
    or csv files first need to be read and converted to a file format that can be memory mapped. Another downside is
    that the OS determines when pages will be swapped. Operations that need a full data shuffle, such as
    sorts, have terrible performance on memory mapped data.
  - Polars' out of core processing is not based on memory mapping, but on streaming data in batches (and spilling to disk
    if needed), we control which data must be hold in memory, not the OS, meaning that we don't have unexpected IO stalls.

- DuckDB

  - Polars and DuckDB have many similarities. DuckDB is focused on providing an in-process OLAP Sqlite alternative,
    polars is focused on providing a scalable `DataFrame` interface to many languages. Those different front-ends lead to
    different optimization strategies and different algorithm prioritization. The interop between both is zero-copy.
    See more: https://duckdb.org/docs/guides/python/polars

- Spark

  - Spark is designed for distributed workloads and uses the JVM. The setup for spark is complicated and the startup-time
    is slow. On a single machine Polars has much better performance characteristics. If you need to process TB's of data
    spark is a better choice.

- CuDF

  - GPU's and CuDF are fast!
    However, GPU's are not readily available and expensive in production. The amount of memory available on GPU often
    is a fraction of available RAM.
    This (and out-of-core) processing means that polars can handle much larger data-sets.
    Next to that Polars can be close in [performance to CuDF](https://zakopilo.hatenablog.jp/entry/2023/02/04/220552).
    CuDF doesn't optimize your query, so is not uncommon that on ETL jobs polars will be faster because it can elide
    unneeded work and materialization's.

- Any

  - Polars is written in Rust. This gives it strong safety, performance and concurrency guarantees.
    Polars is written in a modular manner. Parts of polars can be used in other query program and can be added as a library.

## Acknowledgements

Development of `Polars` is proudly powered by

[![Xomnia](https://raw.githubusercontent.com/pola-rs/polars-static/master/sponsors/xomnia.png)](https://www.xomnia.com)
