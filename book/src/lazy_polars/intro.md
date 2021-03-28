# Lazy Polars
We directly skip the eager API and dive into the lazy API of Polars. We will be exploring its functionality by exploring
two medium large datasets of usernames; the [reddit usernames dataset](https://www.reddit.com/r/datasets/comments/9i8s5j/dataset_metadata_for_69_million_reddit_users_in/)
containing 69+ Million rows and a [runescape username dataset](https://github.com/RuneStar/name-cleanup-2014) containing
55+ Million rows.

Let's write our first lines of Polars and see what kind of data we got. If you haven't done this already you can install
polars from PyPi: `$ pip install --upgrade polars`

## Reddit data
```python
{{#include ../examples/lazy_chapter/data_head.py:0:4}}
```

```text
{{#include ../outputs/head_reddit.txt}}
```

## Runescape data
```python
{{#include ../examples/lazy_chapter/data_head.py:9:10}}
```

```text
{{#include ../outputs/head_runescape.txt}}
```

As we can see, Polars pretty prints the DataFrames and includes a header with column names and the data type of that column.
If you want to learn more about the data types Polars supports, 
see the [Rust reference](POLARS_API_LINK/datatypes/enum.AnyType.html#variants) for a proper
description and the [Python reference](POLARS_API_LINK/datatypes.html) for the wrappers in Python.

Ok, that's easy enough. Next section we get into more interesting stuff. We will take a look at some optimizations Polars 
does regarding predicates.
