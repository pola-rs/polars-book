# Introduction

This book is an introduction to the Polars DataFrame library. The goal is to explain the inner workings of Polars
by going through several examples and making comparisons to other solutions. We'll discuss what some design choices 
have been and how you can use Polars optimally.

Even though Polars is a Rust library the examples shown will be using the Python wrappers. The Python api is the easiest
to get started with and allows easier experimentation.

## Goals and non-goals
The goal of Polars is being a fast DataFrame library that utilizes the available cores on your machine. Its ideal use case
is data too big for pandas and too small for spark. Similar to spark Polars consists of a query planner that may 
(and probably does) optimize your query in order to do less work or reduce memory usage.

However if you really have big data that doesn't fit in memory of a single machine (even after filtering), Polars is not
the solution to your problem.

Polars is completely written in Rust and has no runtime overhead. Python bindings are exposed, but are merely a thin 
wrapper and will not expose more functionality than the Rust library does.

It consists of an eager api that is similar to pandas. With eager we mean that an operation is immediately executed and
produces a result.

The lazy api processes an interpretation of your query called a Logical Plan. This plan is optimized and reordered to 
reduce query time and memory usage. When a result is requested Polars distributes the available work to different 
 `Executors` that use the algorithm available in the eager api to produce a result. Because the whole query context is
 known to the optimizer and executors of the logical plan, processes dependent on separate data sources can be parallelized
 on the fly.

![api](../img/api_polars.svg)


### Current status
This is a concise summary of the features that allow Polars to meet its goals.

* Copy on write semantics
    * "Free" clones
    * Cheap appends
* Column oriented data storage 
    - No block manager (i.e. predictable performance)
* Missing values indicated with bitmask
    - NaN != Missing
    - allows for bitmask optimizations
* Appending without clones
* Efficient algorithms
    * Joins
    * Groupby
    * Sorting
    * Melts
    * Explodes
    * Pivots
    * And more...
* Query optimizations
    - Predicate pushdown
        * filtering at scan level
    - Projection pushdown
        * projection at scan level
    - Simplify expressions
    - Parallel execution of Physical plan
* SIMD vectorization
* numpy ufuncs work on Polars Series
    
## Possibilities
* Memory mapped files
    - Out of core analysis.

## Acknowledgements
Development of Polars is proudly powered by

[![Xomnia](https://raw.githubusercontent.com/ritchie46/img/master/polars/xomnia_logo.png)](https://www.xomnia.com)