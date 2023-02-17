# Using the lazy API
On the page we see how to use the lazy API and look at the role of the schema in the lazy API.

## Using the lazy API from a file
Let's create a lazy query that starts with loading data from the Reddit CSV data and filter on a few predicates. We are using the lazy API here because we start the query with `pl.scan_csv` instead of `pl.read_csv`

```python
{{#include ../../examples/predicate_pushdown/snippet1.py:10}}
```

A `pl.scan_` function is available for a number of file types including CSV, Parquet, Arrow and newline delimited JSON.

## Using the lazy API from a `DataFrame`
An alternative way to access the lazy API is to call `.lazy()` on a `DataFrame` that has already been created.

```python
{{#include ../../examples/predicate_pushdown/snippet3.py:4}}
```

## Knowing the schema in the lazy API
The schema of a Polars `DataFrame` or `LazyFrame` sets out the names of the columns and their datatypes. You can see the schema at any point with the `schema` method on a `DataFrame` or `LazyFrame` 
```python
{{#include ../../examples/predicate_pushdown/snippet3.py:6:6}}
```

```text
{{#include ../../outputs/predicate_pushdown/output4.txt}}
```

To use the lazy API Polars must know the schema at every step of a query plan. This means that operations where the schema is not knowable in advance can not be used with the lazy API.

The classic example of an operation where the schema is not knowable in advance is a `pivot` operation. With a `pivot` the column names come from data in one of the columns. As these data cannot be known in advance a `pivot` cannot be used in the lazy API.
