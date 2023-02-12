# Lazy API key concepts

## Creating a lazy query
Let's load some Reddit data and filter on a few predicates. We use the lazy API here because we start the query with `pl.scan_csv` instead of `pl.read_csv`

```python
{{#include ../../examples/predicate_pushdown/snippet1.py:10}}
```

When we use a `pl.scan_` function we start a query in lazy mode. A `pl.scan_` function is available for a number of file types including CSV, Parquet, Arrow and newline delimited JSON.

An alternative way to access the lazy API is to call `.lazy()` on a `DataFrame` that has already been created.

```python
{{#include ../../examples/predicate_pushdown/snippet3.py:4}}
```



## Role of the schema in the lazy API
The schema of a Polars `DataFrame` or `LazyFrame` sets out the names of the columns and their datatypes. You can see the schema at any point with the `schema` method on a `DataFrame` or `LazyFrame` 
```python
{{#include ../../examples/predicate_pushdown/snippet3.py:6:6}}
```

```text
{{#include ../../outputs/predicate_pushdown/output4.txt}}
```

To use the lazy API Polars must know the schema at every step of a query plan. This means that operations where the schema is not knowable in advance can not be used with the lazy API.

The classic example of an operation where the schema is not knowable in advance is a `pivot` operation. With a `pivot` the column names come from data in one of the columns. As these data cannot be known in advance a `pivot` cannot be used in the lazy API.

## Query execution
If we were to run the code above on the Reddit CSV the query would not be evaluated. Instead Polars takes each line of code and adds it to the internal query graph. This allows Polars to see the whole context of a query. After each line of code Polars optimizes the query graph and this optimized query graph will eventually be executed.


### Execution on the full dataset
Execution is requested by calling the `.collect` method on the query. The  `.collect` method would query all available data.
```python
{{#include ../../examples/predicate_pushdown/snippet4.py}}
```
```text
{{#include ../../outputs/predicate_pushdown/output5.txt}}
```
Above we see that from the 10 Million rows, 656 rows match our predicate.

With the default `collect` method Polars processes all of your data as one batch. This means that the data has to fit into your available memory at the point of peak memory usage in your query.

### Execution on larger-than-memory data

If your data requires more memory than you have available Polars may be able to process the data in batches using the *streaming* mode. To use streaming mode you simply pass the `streaming=True` argument to `collect`
```python
{{#include ../../examples/predicate_pushdown/snippet5.py}}
```

### Execution on a partial dataset

While you're writing, optimizing, and checking your query on a large dataset, querying all available data may lead to a slow development process. In this scenario you can instead execute the query with the `.fetch` method. `.fetch` takes a parameter `n_rows` and tries to 'fetch' that number of rows at the data source (no guarantees are given though).

So let's "fetch" ~10 Million rows from the source file and apply the predicates.

```python
q1.fetch(n_rows=int(1e7))
```

```text
{{#include ../../outputs/predicate_pushdown/output1.txt}}
```


## Understanding a query plan

In `Polars` we can visualize both the non-optimized and optimized query plans. First we visualise the non-optimized plan by setting `optimized=False`.

```python
q1.show_graph(optimized=False)
```

![](../../outputs/predicate_pushdown/graph1.png)

We can also print the non-optimized plan with `describe_plan`

```python
{{#include ../../examples/predicate_pushdown/snippet1.py:10:10}}
```
```text
{{#include ../../outputs/predicate_pushdown/output7.txt}}
```

Whether we use the visualization or the printed plan we read it from bottom to top. This non-optimized plan is roughly to:
- get the full dataset from the `data/reddit.csv` file
- apply the first filter on the `comment_karma` column
- apply the second filter on the `link_karma` column
- apply the third filter on the `name` column

We see how to visualize the optimized plan in the following page.
