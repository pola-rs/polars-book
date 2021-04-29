# How can I determine group statistics?

## Differences in a Group

This example shows how you would determine differences per group. Let's imagine we have a dataset with
some unique identifier **uid** (think a country, state, hospital, etc.), some dates per **uid** as **date** column, and a number of cumulative COVID cases per
**date**. 

Now we want to find to determine the difference (e.g. the increase of COVID cases per day per group.)

First we do this with a self join, and next we will explore the power of window functions.

## Dataset setup
First we create the example dataset of this problem.

```python
{{#include ../examples/how_can_i/det_group_statistics.py:1:24}}
print(df)
```

```text
{{#include ../outputs/det_group_statistics_1.txt}}
```


## Query with a self join
```python
{{#include ../examples/how_can_i/det_group_statistics.py:25:58}}
print(out.collect())
```

```text
{{#include ../outputs/det_group_statistics_2.txt}}
```

## Window functions 💪

Now let's see how we can remove this whole self join with window functions. A window function determines an aggregation
per group and then joins the result back on the column implicitly. Besides, doing this join for you, Polars can also do
this efficiently because it can cache intermediate groupby results and share that between window functions.

Let's first see how we can replace the join with a window function:

```python
{{#include ../examples/how_can_i/det_group_statistics.py:62:71}}
print(out1.collect())
```

```text
{{#include ../outputs/det_group_statistics_3.txt}}
```

Ok, let's break it down. First we apply this window expression: `col("cumcases").apply(mkdiff).over("country")`.
This means we aggregate the diff values in a `list` and we join that back on the original DataFrame `base_df`.
This column thus is a `Series` containing lists.

Then with `.take(col("country").arg_unique())`, we select only the lists that correspond with the first unique value in
the `"country"` column. That would lead to a `Series` with 3 list values, one for each country. Then finally, we explode
(flatten the list of lists) that column, which makes the column fit on the original DataFame.

## Combining window functions

These window functions can be used in a `with_columns`, or `select` as much as needed. This can be used to easily create
different group statistics in one go.

```python
{{#include ../examples/how_can_i/det_group_statistics.py:72:85}}
print(out2.collect())
```

```text
{{#include ../outputs/det_group_statistics_4.txt}}
```
