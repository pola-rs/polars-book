# Query execution

Our example query on the Reddit dataset is:

```python
{{#include ../examples/lazy_api/snippet1.py::10}}
```

If we were to run the code above on the Reddit CSV the query would not be evaluated. Instead Polars takes each line of code, adds it to the internal query graph and optimizes the query graph.

When we execute the code Polars executes the optimized query graph by default.

### Execution on the full dataset

We can execute our query on the full dataset by calling the `.collect` method on the query.

```python
{{#include ../examples/lazy_api/snippet4.py}}
```

```text
{{#include ../outputs/lazy_api/df4.txt}}
```

Above we see that from the 10 Million rows there 14,029 rows match our predicate.

With the default `collect` method Polars processes all of your data as one batch. This means that all the data has to fit into your available memory at the point of peak memory usage in your query.

### Execution on larger-than-memory data

If your data requires more memory than you have available Polars may be able to process the data in batches using *streaming* mode. To use streaming mode you simply pass the `streaming=True` argument to `collect`

```python
{{#include ../examples/lazy_api/snippet5.py}}
```

We look at [streaming in more detail here](streaming.md).

### Execution on a partial dataset

While you're writing, optimizing or checking your query on a large dataset, querying all available data may lead to a slow development process.

You can instead execute the query with the `.fetch` method. The `.fetch` method takes a parameter `n_rows` and tries to 'fetch' that number of rows at the data source. The number of rows cannot be guaranteed, however, as the lazy API does not count how many rows there are at each stage of the query.

Here we "fetch" 100 rows from the source file and apply the predicates.

```python
{{#include ../examples/lazy_api/snippet9.py}}
```

```text
{{#include ../outputs/lazy_api/q9.txt}}
```
