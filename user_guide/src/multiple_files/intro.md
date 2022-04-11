## Dealing with multiple files.

`Polars` can deal with multiple files differently depending on your needs and memory strain.

Let's create some files to give use some context:

```python
{{#include ../examples/multiple_files/dataset.py:0:}}
```

## Reading into a single `DataFrame`

To read multiple files into a single `DataFrame`, we can use globbing patterns:

```python
{{#include ../examples/multiple_files/single_df.py:3:}}
print(df)
```

```text
{{#include ../outputs/multiple_files/single_df.txt}}
```

To see how this works we can take a look at the query plan. Below we see that all files are read separately and
concatenated into a single `DataFrame`. `Polars` will try to parallelize the reading.

```python
pl.scan_csv("my_many_files_*.csv").show_graph()
```

![single_df_graph](../outputs/multiple_files/single_df_graph.png)

## Reading and processing in parallel

If your files don't have to be in a single table you can also build a query plan for each file and execute them in paralllel
on the `Polars` thread pool.

All query plan execution is embarrassingly parallel and doesn't require any communication.

```python
{{#include ../examples/multiple_files/multiple_queries.py:1:}}
print(dataframes)
```

```text
{{#include ../outputs/multiple_files/dataframes.txt}}
```
