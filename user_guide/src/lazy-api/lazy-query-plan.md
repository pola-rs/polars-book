# Understanding a query plan

In `Polars` we can visualize both the non-optimized and optimized query plans.

## Non-optimized query plan
First we visualise the non-optimized plan by setting `optimized=False`.

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

## Optimized query plan
With query optimization in the lazy API `Polars` saves that mental overhead from the query writer and combines predicates for you (we appreciate that this is hard to see in the visualisation!). 

```python
q1.show_graph(optimized=True)
```

![](../../outputs/predicate_pushdown/graph1-optimized.png)

We can also print the optimized plan with `describe_optimized_plan`
```python
{{#include ../../examples/predicate_pushdown/snippet1.py:16:16}}
```
```text
{{#include ../../outputs/predicate_pushdown/output9.txt}}
```
