# Streaming larger-than-memory datasets

When a lazy query is executed in streaming mode Polars processes the dataset in batches rather than all-at-once. This can allow Polars to process datasets that are larger-than-memory.

To tell Polars we want to execute a query in streaming mode we pass the `streaming=True` argument to `collect`

```python
{{#include ../examples/lazy_api/snippet5.py}}
```

We can also use streaming mode when we execute lazy queries in other ways such as a partial execution with `fetch` or a profiling execution with `profile`.

## When is streaming available?

Streaming is still a developing feature of Polars. We can ask Polars to execute any lazy query in streaming mode. However, not all lazy operations support streaming. If there is an operation for which streaming is not supported Polars will run the query in non-streaming mode.

Streaming is supported for many operations including:

- `filter`,`slice`,`head`,`tail`
- `with_columns`,`select`
- `groupby`,`groupby_dynamic`
- `join`,`join_asof`
- `sort`
- `scan_csv`,`scan_parquet`,`scan_ipc`

## Sinking to a file

Although streaming allows you to process larger than memory datasets the output `DataFrame` must still fit in memory.

To work with data where the output `DataFrame` is too large to fit in memory we can write it directly to disk. We use streaming to do this by executing the lazy query with a `sink_` function instead of `collect`. The `sink_` functions use streaming by default.

```python
{{#include ../examples/lazy_api/snippet11.py}}
```

There are `sink_` functions available to write to [Parquet](POLARS_PY_REF_GUIDE/lazyframe/api/polars.LazyFrame.sink_parquet.html) and [IPC](POLARS_PY_REF_GUIDE/lazyframe/api/polars.LazyFrame.sink_ipc.html) file formats.
