# Using the lazy API

Here we see how to use the lazy API starting from either a file or an existing `DataFrame`.

## Using the lazy API from a file

In the ideal case we use the lazy API right from a file as the query optimizer may help us to reduce the amount of data we read from the file.

We create a lazy query from the Reddit CSV data and apply some transformations.

By starting the query with `pl.scan_csv` we are using the lazy API.

```python
{{#include ../examples/lazy_api/snippet1.py::9}}
```

A `pl.scan_` function is available for a number of file types including [CSV](POLARS_PY_REF_GUIDE/api/polars.scan_csv.html), [Parquet](POLARS_PY_REF_GUIDE/api/polars.scan_parquet.html), [IPC](POLARS_PY_REF_GUIDE/api/polars.scan_ipc.html) and [newline delimited JSON](POLARS_PY_REF_GUIDE/api/polars.scan_ndjson.html).

In this query we tell Polars that we want to:

- load data from the Reddit CSV file
- convert the `name` column to uppercase
- apply a filter to the `comment_karma` column

The lazy query will not be executed at this point. See this page on [executing lazy queries](lazy-query-execution.md) for more on running lazy queries.

## Using the lazy API from a `DataFrame`

An alternative way to access the lazy API is to call `.lazy` on a `DataFrame` that has already been created in memory.

```python
{{#include ../examples/lazy_api/snippet3.py:4:4}}
```

By calling `.lazy` we convert the `DataFrame` to a `LazyFrame`.
