# 10 Minutes to Polars
 
To help you get started this notebook introduces some of the key concepts that make Polars a powerful data analysis tool. 

The key concepts we meet are:
- fast flexible analysis with the **Expression API** in Polars
- easy **parallel** computations
- automatic **query optimisation** in **lazy mode**
- **streaming** to work with larger-than-memory datasets in Polars

## Importing Polars
We begin by importing polars as `pl`


```python
import polars as pl
```

## Setting configuration options
Before we start exploring a dataset we are going to control how a `DataFrame` is print on the screen. We control configuration using options in `pl.Config` - [see the API docs for the full range](https://pola-rs.github.io/polars/py-polars/html/reference/config.html).

In this notebook we want Polars to:
- print up to 6 rows of each `DataFrame` so we use `pl.Config.set_tbl_rows` and 
- print up to 10 columns of each `DataFrame` so we use `pl.Config.set_tbl_cols`


```python
{{#include ../examples/tutorials/10_minutes_to_polars/creating_a_dataframe.py:3:4}}
```





    polars.cfg.Config



We also want strings to be printed with up to 30 characters 


```python
{{#include ../examples/tutorials/10_minutes_to_polars/creating_a_dataframe.py:6:6}}
```




    polars.cfg.Config



You can find the [full range of configuration options in the API docs](POLARS_PY_REF_GUIDE/config.html).

## Creating a `DataFrame`
Polars can read from a wide range of data formats including CSV, Parquet, Arrow, JSON, Excel and database connections. See the [I/O section of the User Guide](/howcani/io/intro.html) for more information.

For this introduction we use a CSV with the Titanic passenger dataset. This dataset gives details of all the passengers on the Titanic and whether they survived.

We begin by setting the url of the CSV


```python
csv_url = "https://raw.githubusercontent.com/pola-rs/polars-static/master/data/titanic.csv"
```

We read the CSV into a Polars `DataFrame` with the `read_csv` function. We then call `head` on the `DataFrame` to print out the first few rows of the `DataFrame`


```python
{{#include ../examples/tutorials/10_minutes_to_polars/creating_a_dataframe.py:10:10}}
print(df.head(3))
```

```text
{{#include ../outputs/tutorials/10-minutes-to-polars/df_head.txt}}
```


Each row of this `DataFrame` has details about a passenger on the Titanic including the class they travelled in (`Pclass`), their name (`Name`) and `Age`.

When we print out a `DataFrame` we get the shape and the dtype of each column below the column name.

Note that a Polars `DataFrame` does not have an index. The lack of an index saves developer effort in setting and resetting the index.

## Accessing and transforming data

### Using square brackets

While you can use square brackets to select rows and columns in Polars...

```python
{{#include ../examples/tutorials/10_minutes_to_polars/creating_a_dataframe.py:12:12}}
print(square_brackets_df)
```

```text
{{#include ../outputs/tutorials/10-minutes-to-polars/square_brackets_df.txt}}
```

...this square bracket approach means that you won't get all the benefits of parallelisation, query optimisation and scalability that we see below. 

To really take advantage of Polars we use the Expression API to access and transform data.

### Selecting and transforming columns with the Expression API

We see a first example of the Expression API here where we select the `Pclass`, `Name` and `Age` columns inside a `select` statement


```python
{{#include ../examples/tutorials/10_minutes_to_polars/creating_a_dataframe.py:12:18}}
print(select_df)
```

```text
{{#include ../outputs/tutorials/10-minutes-to-polars/select_df.txt}}
```

In the Expression API we begin the expression by using `pl.col` to select to a column. We call the operation on each column an **expression**

### Transforming columns in the Expression API 
The Expression API allows us not only to select columns but also to transform them.

Here we select the same three columns, but with some transformations in each expression before we return them:
- we convert the integers in `Pclass` to the utf-8 string dtype with `cast`
- we get the number of words in each name with `str.to_lowercase` and
- we round off the age to the nearest whole number with `round`


```python
{{#include ../examples/tutorials/10_minutes_to_polars/creating_a_dataframe.py:12:14}}
print(select_transform_df)
```

```text
{{#include ../outputs/tutorials/10-minutes-to-polars/select_transform_df.txt}}
```

In this example we passed multiple expressions to `select`. When we have multiple expressions Polars runs them in parallel. This is one example of how Polars handles parallelisation automatically.

### Chaining expressions
We chain expressions together to do multi-stage transformations on a column. 

In this example we output the name and count the number of words in each name by:
- splitting the `Name` column into a list of words with `str.split` and then
- counting the length of each list with `arr.lengths`

We add the word count as a new column by giving it an `alias` at the end of the expression

```python
{{#include ../examples/tutorials/10_minutes_to_polars/select_chain.py:12:17}}
print(select_chain)
```

```text
{{#include ../outputs/tutorials/10-minutes-to-polars/select_chain_df.txt}}
```


## Adding a column
In the examples above we use `select` to return a subset of columns. To add a new column to the full `DataFrame` we use `with_column`


```python
{{#include ../examples/tutorials/10_minutes_to_polars/with_columns.py:12:17}}
print(with_columns_df)
```

```text
{{#include ../outputs/tutorials/10-minutes-to-polars/with_columns_df.txt}}
```


Square brackets **cannot** be used to add new columns, so the following **does not work**
```python
df["Fare_rounded"] = df["Fare"].round(1)
```


### Filtering a `DataFrame`

We filter a `DataFrame` by applying a condition in an expression.

In this example we find all the passengers over 70 years of age


```python
{{#include ../examples/tutorials/10_minutes_to_polars/filter_dataframe.py:12:12}}
print(filtered_df)
```

```text
{{#include ../outputs/tutorials/10-minutes-to-polars/filtered_df.txt}}
```

We can specify multiple conditions with the `&` operator

```python
{{#include ../examples/tutorials/10_minutes_to_polars/filter_dataframe_and.py:12:12}}
print(joint_filtered_df)
```

```text
{{#include ../outputs/tutorials/10-minutes-to-polars/joint_filtered_df.txt}}
```

### Groupby and aggregations
Here we look at passenger survival by class.
- We first group by the `Survived` and the `Pclass` columns 
- We aggregate by counting the number of passengers in each group
- We aggregate by getting the average age in each group

```python
{{#include ../examples/tutorials/10_minutes_to_polars/groupby_dataframe.py:12:14}}
print(grouped_df)
```

```text
{{#include ../outputs/tutorials/10-minutes-to-polars/grouped_df.txt}}
```

Note that we use the Expression API for each aggregation in `agg`. We do multiple aggregations in this case by with a `list` inside `agg`.

Groupby operations in Polars are fast because Polars has a parallel algorithm for getting the groupby keys. Aggregations are also fast because Polars runs multiple expressions in `agg` in parallel.

## Lazy mode and query optimisation
In the examples above we work in eager mode. In eager mode Polars runs each part of a query step-by-step.

Polars has a powerful feature called lazy mode. In lazy mode Polars adds each part of a query to a query graph.  

**Running in lazy mode is crucial allowing Polars to apply query optimisation and to work with larger-than-memory datasets.** 

Before running the code Polars passes the query graph through its optimiser to see if there ways to make the query faster.

When working from a CSV we work in lazy mode instead of eager mode by replacing `read_csv` with `scan_csv`. When we use `scan_csv` the output is a `LazyFrame` rather than a `DataFrame` and Polars prints the non-optimised *naive* plan associated with this `LazyFrame`


```python
{{#include ../examples/tutorials/10_minutes_to_polars/groupby_dataframe_lazy.py:10:14}}
print(lazy_grouped_df)
```

```text
{{#include ../outputs/tutorials/10-minutes-to-polars/lazy_grouped_df.txt}}
```
### Query optimiser
We see the optimised query plan by calling the `describe_optimized_plan` method on a `LazyFrame`

```python
{{#include ../examples/tutorials/10_minutes_to_polars/groupby_dataframe_lazy.py:16:16}}
print(lazy_grouped_plan)
```

```text
{{#include ../outputs/tutorials/10-minutes-to-polars/lazy_grouped_plan.txt}}
```

The output of a lazy query is a `LazyFrame` and we see the graph of the unoptimized query plan when we output a `LazyFrame`.

### Projection pushdown optimisation
In this example Polars has identified an optimisation and we see this on the second last line of the optimised query plan:
```python
PROJECT 4/9 COLUMNS
```
There are 9 columns in the CSV, but the query optimiser sees that only 4 of these columns are required for the query. When the query is evaluated Polars will `PROJECT` 4 out of 9 columns. This means that Polars will only read the 4 required columns from the CSV. 

This optimisation is called a *projection pushdown*. This projection saves memory and computation time.


### Predicate pushdown optimisation

A different optimisation happens when we add a `filter` to a query. In this case we want the same analysis of survival by class but only for passengers over 50


```python
{{#include ../examples/tutorials/10_minutes_to_polars/filter_dataframe_lazy.py:10:17}}
print(lazy_filter_grouped_df)
```

```text
{{#include ../outputs/tutorials/10-minutes-to-polars/lazy_filter_grouped_df.txt}}
```
    
    


In this example the query optimiser has seen that:
- 4 out of 9 columns are required and
- only passengers over 50 should be selected: `SELECTION: Some([(col("Age")) > (50f64)])`

This optimisation with a filter is called a *predicate pushdown* where the predicate is the condition 
```python
pl.col("Age") > 50
```

These optimisations are applied as Polars reads the CSV file so the whole dataset is not read into memory.

### Query evaluation

#### Full evaluation
To evaluate the query for all output rows we call `collect` 


```python
{{#include ../examples/tutorials/10_minutes_to_polars/evaluate_dataframe_lazy.py:10:16}}
print(evaluate_grouped_df)
```

```text
{{#include ../outputs/tutorials/10-minutes-to-polars/evaluate_grouped_df.txt}}
```


#### Limited evaluation

During development with a large dataset it may be better to limit evaluation to a smaller number of output rows. We can do this by replacing `collect` with `fetch`


```python
{{#include ../examples/tutorials/10_minutes_to_polars/evaluate_dataframe_lazy.py:18:24}}
print(evaluate_grouped_df)
```

```text
{{#include ../outputs/tutorials/10-minutes-to-polars/fetch_grouped_df.txt}}
```

Calling `fetch` is similar to a `LIMIT` clause in a SQL query.

## Streaming larger-than-memory datasets
By default Polars reads your full dataset into memory when evaluating a lazy query. 

However, if your dataset is too large to fit into memory Polars can run many core operations in *streaming* mode. With streaming Polars processes your query in batches rather than all at once. This allows Polars to scale to larger-than-memory datasets.

To enable streaming we pass the `streaming = True` argument to `collect`


```python
{{#include ../examples/tutorials/10_minutes_to_polars/evaluate_dataframe_lazy.py:26:32}}
print(stream_grouped_df)
```

```text
{{#include ../outputs/tutorials/10-minutes-to-polars/stream_grouped_df.txt}}
```



## Summary
This notebook has been a quick overview of the key ideas that make Polars a powerful data analysis tool:
- expressions allow us to write complex transformations concisely and run them in parallel
- lazy mode allows Polars apply query optimisations that reduce memory usage and computation time
- streaming lets us process larger-than-memory datasets

## Next steps
The next step for you is to try Polars on your own data while going through this User Guide.

If you want more information on each function along with an example of use see the [API reference docs](https://pola-rs.github.io/polars/py-polars/html/reference/).

StackOverflow is a great place to start if you need help. There are many Polars questions on there already and your question might already by answered. If you need to ask a new questions you greatly improve your chances of getting help if you provide a minimal working example with some sample inputs, target outputs and your own best effort [as in this example](https://stackoverflow.com/questions/74562243/how-to-perform-split-merge-melt-with-python-and-polars). 

You should also [check in with the Polars community on Discord](https://discord.com/invite/4UfP5cfBE7). This is a great place to chat about how you are using Polars and how you think it could develop.


```python

```
