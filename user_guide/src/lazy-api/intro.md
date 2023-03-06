# Lazy API

With the lazy API Polars doesn't run each query line-by-line but instead processes the full query end-to-end. To get the most out of Polars it is important that you use the lazy API because:

- the lazy API allows Polars to apply automatic query optimization with the query optimizer
- the lazy API allows you to work with larger than memory datasets using streaming
- the lazy API can catch schema errors before processing the data

The pages in this section cover:

- [Using the lazy API](lazy-query-create.md)
- [Schema in the lazy API](lazy-schema.md)
- [Understanding the query plan](lazy-query-plan.md)
- [Executing lazy queries](lazy-query-execution.md)
- [Streaming larger-than-memory datasets](streaming.md)

## Dataset

To demonstrate the lazy `Polars` capabilities we'll explore a medium-large
dataset of usernames.

The [Reddit usernames dataset](https://www.reddit.com/r/datasets/comments/9i8s5j/dataset_metadata_for_69_million_reddit_users_in/)
contains over 69 million rows with data on Reddit users.

```python
{{#include ../examples/lazy_api/snippet10.py}}
```

```text
{{#include ../outputs/lazy_api/dataset.txt}}
```
