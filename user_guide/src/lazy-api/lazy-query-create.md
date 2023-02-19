# Using the lazy API

We see how here how to use the lazy API from either a file or an existing `DataFrame`.

## Using the lazy API from a file

Let's create a lazy query that starts with loading data from the Reddit CSV data and apply some transformations.

We are using the lazy API here because we start the query with `pl.scan_csv` instead of `pl.read_csv`

```python
{{#include ../examples/lazy_api/snippet1.py::10}}
```

In this query we:

- load data from the Reddit CSV file
- convert the `name` column to uppercase
- apply a filter to the `comment_karma` column

A `pl.scan_` function is available for a number of file types including [CSV](POLARS_PY_REF_GUIDE/api/polars.scan_csv.html), [Parquet](POLARS_PY_REF_GUIDE/api/polars.scan_parquet.html), [IPC](POLARS_PY_REF_GUIDE/api/polars.scan_ipc.html) and [newline delimited JSON](POLARS_PY_REF_GUIDE/api/polars.scan_ndjson.html).

## Using the lazy API from a `DataFrame`

An alternative way to access the lazy API is to call `.lazy()` on a `DataFrame` that has already been created.

```python
{{#include ../examples/lazy_api/snippet3.py::4}}
```
