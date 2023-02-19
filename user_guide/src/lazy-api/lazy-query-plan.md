# Understanding a query plan

For any lazy query `Polars` has both:

- the non-optimized plan that reflects the code as we provide it and
- the optimized plan with any changes made by the query optimizer

We can understand both the non-optimized and optimized query plans with visualization and by printing them.

## Non-optimized query plan

### Graphviz visualization

First we visualise the non-optimized plan by setting `optimized=False`.

```python
{{#include ../examples/lazy_api/snippet1.py:19:19}}
```

![](../outputs/lazy_api/graph1.png)

The visualisation should be read from bottom to top. In the visualisation:

- each box corresponds to a stage in the query plan
- the `\sigma` stands for `SELECTION` and indicates any filter conditions
- the `\pi` stands for `PROJECTION` indicates choosing a subset of columns

### Printed query plan

We can also print the non-optimized plan with `describe_plan`

```python
{{#include ../examples/lazy_api/snippet1.py:11:11}}
```

```text
{{#include ../outputs/lazy_api/q1_plan.txt}}
```

The printed plan should also be read from bottom to top. This non-optimized plan is roughly to:

- get the full dataset from the `data/reddit.csv` file
- transform the `name` column to uppercase
- apply a filter on the `comment_karma` column

## Optimized query plan

With query optimization in the lazy API `Polars` saves the mental overhead of manually combining filter predicates into a single `filter` and combines predicates for you. We can see this in the visualization with the default arguments for `show_graph`

```python
{{#include ../examples/lazy_api/snippet1.py:21:21}}
```

![](../outputs/lazy_api/graph1-optimized.png)

We can also print the optimized plan with `describe_optimized_plan`

```python
{{#include ../examples/lazy_api/snippet1.py:15:15}}
```

```text
{{#include ../outputs/lazy_api/q1_opt_plan.txt}}
```

The optimized plan is to:

- read the data from the Reddit CSV applying the filter while reading the CSV file line-by-line
- transform the `name` column to uppercase
