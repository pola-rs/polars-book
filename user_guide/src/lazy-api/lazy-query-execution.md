# Query execution

Our example query on the Reddit dataset is:

```python
{{#include ../examples/lazy_api/snippet1.py::10}}
```

If we were to run the code above on the Reddit CSV the query would not be evaluated. Instead Polars takes each line of code, adds it to the internal query graph and optimizes the query graph.

When we execute the code Polars executes the optimized query graph by default.

### Execution on the full dataset

Execution is requested on the full dataset by calling the `.collect` method on the query.

```python
{{#include ../examples/lazy_api/snippet4.py}}
```

```text
{{#include ../outputs/lazy_api/output5.txt}}
```

Above we see that from the 10 Million rows, 14,029 rows match our predicate.

With the default `collect` method Polars processes all of your data as one batch. This means that the data has to fit into your available memory at the point of peak memory usage in your query.

### Execution on larger-than-memory data

If your data requires more memory than you have available Polars may be able to process the data in batches using the *streaming* mode. To use streaming mode you simply pass the `streaming=True` argument to `collect`

```python
{{#include ../examples/lazy_api/snippet5.py}}
```

### Execution on a partial dataset

While you're writing, optimizing, and checking your query on a large dataset, querying all available data may lead to a slow development process. In this scenario you can instead execute the query with the `.fetch` method. `.fetch` takes a parameter `n_rows` and tries to 'fetch' that number of rows at the data source (no guarantees are given though).

So let's "fetch" ~10 Million rows from the source file and apply the predicates.

```python
{{#include ../examples/lazy_api/snippet9.py}}
```

```python
q1.fetch(n_rows=int(1e7))
```

```text
{{#include ../outputs/lazy_api/output9.txt}}
```
