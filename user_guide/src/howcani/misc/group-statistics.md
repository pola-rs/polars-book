# Determine group statistics

This example shows how one would idiomatically determine differences per group.
Let's imagine we have a dataset with some countries, some dates per country and a number of cumulative [COVID](https://en.wikipedia.org/wiki/COVID-19_pandemic) cases per date.

Let's determine the differences, *e.g.* the increase of COVID cases per day, per group.

## Dataset

```python
{{#include ../../examples/group_statistics/dataset.py}}
```

providing:

```text
{{#include ../../outputs/group_statistics/dataset.txt}}
```

## Self join

The most straightforward way to compute what we want:

```python
{{#include ../../examples/group_statistics/snippet1.py}}
```

yielding:

```text
{{#include ../../outputs/group_statistics/output1.txt}}
```

## Window functions

Now let's see how we can replace the self join with window functions.
A window function determines an aggregation per group before joining the result back on the column implicitly.
`Polars` does this efficiently by caching intermediate grouping results and sharing between window functions.

Let's first see how we can replace the join with a window function:

```python
{{#include ../../examples/group_statistics/snippet2.py}}
```

returning:

```text
{{#include ../../outputs/group_statistics/output2.txt}}
```

Let's break it down:

1. First we apply the following window expression: `pl.col("cumcases").apply(mkdiff).over("country")`.
   This means we aggregate the difference values in a `list` and we join that back on the original DataFrame `base_df`.
   This column is a `pl.Series` containing lists.
2. Then with `.take(pl.col("country").arg_unique())`, we select only the lists that correspond with the first unique value in the `"country"` column.
   That would lead to a `pl.Series` with 3 `list` values, one for each country present in the dataset.
3. Then finally, we explode (flatten the list of lists) that column, which makes the column fit on the original DataFame.

Window functions can be used within a `.with_columns()` statement, or `.select()` as much as needed.
This can be used to extend the previous snippet and create different group statistics in one go:

```python
{{#include ../../examples/group_statistics/snippet3.py}}
```

returning full blown statistics:

```text
{{#include ../../outputs/group_statistics/output3.txt}}
```
