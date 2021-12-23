<div style="margin: 30px auto; background-color: white; border-radius: 50%; width: 200px; height: 200px;"><img src="https://raw.githubusercontent.com/pola-rs/polars-static/master/logos/polars-logo-dark.svg" alt="Polars logo" style="width: 168px; height: 168px; padding: 10px 20px;"></div>

# Introduction

This book is an introduction to the
[`Polars` DataFrame library](https://github.com/pola-rs/polars). Its goal is to
introduce you to `Polars` by going through examples and comparing it to other
solutions. Some design choices are introduced here, and the optimal use of `Polars`
described.

Even though `Polars` is completely written in [`Rust`](https://www.rust-lang.org/) (no
runtime overhead!) and uses [`Arrow`](https://arrow.apache.org/) -the
[native arrow2 `Rust` implementation](https://github.com/jorgecarleitao/arrow2)- as its foundation, the
examples presented in this guide will be mostly using its higher-level language
bindings. The latter are merely a thin wrapper that will not offer more
functionalities than the core library does.

For people used to [`Pandas`](https://pandas.pydata.org/), the
[`Python`](https://www.python.org/) bindings are the easiest to get started with
`Polars`, allowing easier experimentation.

## Goals and non-goals

The goal of `Polars` is being a lightning fast DataFrame library that utilizes all
available cores on your machine. Unlike tools like dask that tries to parallelize existing single-threaded libraries
like `numpy` and `pandas`, `polars` is written from the ground up with parallelization of DataFrame queries in mind.
It goes through great efforts to reduce redundant copies, traverse memory cache efficiently have minimal contention in
parallelism.

`Polars` is lazy and semi-lazy. It allows you to do most of your work eagerly, similar to `pandas`, but
it does provide you with a powerful expression syntax that will be optimized and executed on polars' query engine.

In lazy `Polars` we are able to do query optimization on your whole queries, further improving performance and memory pressure.

`Polars` keeps track of your query in a *logical plan*. This
plan is optimized and reordered before running it. When a result is requested `Polars`
distributes the available work to different *executors* that use the algorithms available
in the eager API to produce a result. Because the whole query context is known to
the optimizer and executors of the logical plan, processes dependent on separate data
sources can be parallelized on the fly.

![](https://raw.githubusercontent.com/pola-rs/polars-static/master/docs/api.svg)

### Performance 🚀🚀

Polars is very fast, and in fact is one of the best performing solutions available.
See the results in h2oai's db-benchmark. The image below shows the biggest datasets yielding a result.

![](https://www.ritchievink.com/img/post-35-polars-0.15/db-benchmark.png)

### Current status

Below a concise list of the features allowing `Polars` to meet its goals:

- [Copy-on-write](https://en.wikipedia.org/wiki/Copy-on-write) (COW) semantics
  - "Free" clones
  - Cheap appends
- Appending without clones
- Column oriented data storage
  - No block manager (-i.e.- predictable performance)
- Missing values indicated with bitmask
  - NaN are different from missing
  - Bitmask optimizations
- Efficient algorithms
- Very fast IO
  - Its csv and parquet readers are among the fastest in existence
- [Query optimizations](optimizations/lazy/intro.md)
  - Predicate pushdown
    - Filtering at scan level
  - Projection pushdown
    - Projection at scan level
  - Aggregate pushdown
    - Aggregations at scan level
  - Simplify expressions
  - Parallel execution of physical plan
  - Cardinality based groupby dispatch
    - Different groupby strategies based on data cardinality
- SIMD vectorization
- [`NumPy` universal functions](https://numpy.org/doc/stable/reference/ufuncs.html)

## Acknowledgements

Development of `Polars` is proudly powered by

[![Xomnia](https://raw.githubusercontent.com/pola-rs/polars-static/master/sponsors/xomnia.png)](https://www.xomnia.com)
