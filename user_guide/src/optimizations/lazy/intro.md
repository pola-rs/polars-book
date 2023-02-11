# Lazy API

The lazy API is important for optimal queries because: 
- the lazy API allows Polars to apply query optimization automatically with the Polars query optimizer
- the lazy API allows you to work with larger than memory datasets using streaming

## Datasets
To demonstrate the lazy `Polars` capabilities we'll explore two medium-large
datasets of usernames.

### Reddit usernames dataset

The [Reddit usernames dataset](https://www.reddit.com/r/datasets/comments/9i8s5j/dataset_metadata_for_69_million_reddit_users_in/)
contains over 69 million rows with data on Reddit users. 

```python
{{#include ../../examples/head/snippet1.py}}
```

```text
{{#include ../../outputs/head/output1.txt}}
```
### Runescape username dataset
The [Runescape username dataset](https://github.com/RuneStar/name-cleanup-2014)
contains over 55 million records.

```python
{{#include ../../examples/head/snippet2.py}}
```

```text
{{#include ../../outputs/head/output2.txt}}
```
