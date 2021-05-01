# Arrow

`Arrow` is rapidly becoming the _de facto_ standard for columnar data.
This means that support for `Arrow` is growing rapidly, in languages and in tools.
Due to the great effort that is being put in the format, using `Arrow` is now likely the fastest way to:

* Read en write `Parquet` formatted files.
* Read CSV into columnar data.
* Exchanging columnar data.

`Polars` uses `Arrow` memory buffer as the most basic building block for `Polars` `Series`.
This means that we exchange data between `Polars` and `Arrow` **without copying** it.
It also means that where `Arrow` performs well, `Polars` does. 

One can convert a `Polars` `DataFrame` or `Series` to `Arrow` using the `.to_arrow()` method.
Similarly, importing from `Arrow` data structure can be performed with the `.from_arrow()` functions.
