<div style="text-align:center;margin-top:30px"><img src="https://raw.githubusercontent.com/ritchie46/static/master/polars/polars_logo_white_circle.png" width="200px" /></div>

# Introduction

This book is an introduction to the
[`Polars` DataFrame library](https://github.com/ritchie46/polars). Its goal is to
explain the inner workings of `Polars` by going through examples and compare it to other
solutions. Some design choices are here introduced, and the optimal use of `Polars`
described.

Even though `Polars` is completely written in [`Rust`](https://www.rust-lang.org/) (no
runtime overhead!) and uses [`Arrow`](https://arrow.apache.org/) -the
[native `Rust` implementation](https://docs.rs/crate/arrow/3.0.0)- at its fundation, the
examples presented in this guide will be mostly using its higher-level language
bindings. Those latter are merely a thin wrapper that will not offer more
functionalities than the core library does.

For people used to [`Pandas`](https://pandas.pydata.org/), the
[`Python`](https://www.python.org/) bindings are the easiest to get started with
`Polars`, allowing easier experimentation.

## Goals and non-goals

The goal of `Polars` is being a lightning fast DataFrame library that utilizes all
available cores on your machine.

`Polars` is semi-lazy. It allows you to do most of your work eagerly, similar to `pandas`, but
it does provide you with a powerfull expression syntax that will be optimized executed on polars' query engine.

`Polars` also supports full lazy query execution that allows for more query optimization.

`Polars` keeps track of your query in a *logical plan*. This
plan is optimized and reordered before running it. When a result is requested `Polars`
distributes the available work to different *executors* that use the algorithms available
in the eager API to come up with the result. Because the whole query context is known to
the optimizer and executors of the logical plan, processes dependent on separate data
sources can be parallelized on the fly.

![](https://raw.githubusercontent.com/ritchie46/static/master/polars/api.svg)

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
- [Query optimizations](lazy/intro.md)
  - Predicate pushdown
    - Filtering at scan level
  - Projection pushdown
    - Projection at scan level
  - Simplify expressions
  - Parallel execution of physical plan
- SIMD vectorization
- [`NumPy` universal functions](https://numpy.org/doc/stable/reference/ufuncs.html)

## Acknowledgements

Development of `Polars` is proudly powered by

[![Xomnia](https://raw.githubusercontent.com/ritchie46/static/master/polars/xomnia_logo.png)](https://www.xomnia.com)
