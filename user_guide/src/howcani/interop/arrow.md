# Arrow

`Arrow` is rapidly becoming the _de facto_ standard for columnar data. This means that
support for `Arrow` is growing rapidly (both languages and tools). Due to the amazing
effort behind the format, using `Arrow` is now likely the fastest way to:

- Read and write `Parquet` formatted files
- Read CSV into columnar data
- Exchanging columnar data

`Polars` uses an `Arrow` memory buffer as the most basic building block for the `Polars`
`Series`. This means that we exchange data between `Polars` and `Arrow` **without
copying** it. It also means that `Polars` shares the same performance gains that `Arrow` receives.

Convert a `Polars` `DataFrame` or `Series` to `Arrow` using the `.to_arrow()`
method. Similarly, importing from `Arrow` data structure can be performed with the
`.from_arrow()` functions.
