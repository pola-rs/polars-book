# Query Plan

For any lazy query `Polars` has both:

- a non-optimized plan with the set of steps code as we provided it and
- an optimized plan with changes made by the query optimizer

We can understand both the non-optimized and optimized query plans with visualization and by printing them as text.

## Non-optimized query plan

### Graphviz visualization

First we visualise the non-optimized plan by setting `optimized=False`.

=== ":fontawesome-brands-python: Python"
    ``` python
    --8<-- "user-guide/python/lazy/query_plan.py:plan"
    --8<-- "user-guide/python/lazy/query_plan.py:showplan"
    ```

<div style="display:none">
```python exec="on" result="text" session="user-guide/lazy/query_plan"
--8<-- "user-guide/python/lazy/query_plan.py:setup"
--8<-- "user-guide/python/lazy/query_plan.py:plan"
--8<-- "user-guide/python/lazy/query_plan.py:createplan"
--8<-- "user-guide/python/lazy/query_plan.py:createplan2"
```
</div>

![](../../src/images//query_plan.png)

The query plan visualisation should be read from bottom to top. In the visualisation:

- each box corresponds to a stage in the query plan
- the `sigma` stands for `SELECTION` and indicates any filter conditions
- the `pi` stands for `PROJECTION` and indicates choosing a subset of columns

### Printed query plan

We can also print the non-optimized plan with `describe_plan`

=== ":fontawesome-brands-python: Python"
    ``` python
    --8<-- "user-guide/python/lazy/query_plan.py:describe"
    ```

```text
FILTER [(col("comment_karma")) > (0)] FROM WITH_COLUMNS:
 [col("name").str.uppercase()]

    CSV SCAN data/reddit.csv
    PROJECT */6 COLUMNS
```

The printed plan should also be read from bottom to top. This non-optimized plan is roughly to:

- read from the `data/reddit.csv` file
- read all 6 columns (where the * wildcard in PROJECT \*/6 COLUMNS means take all columns)
- transform the `name` column to uppercase
- apply a filter on the `comment_karma` column

## Optimized query plan

Now we visualise the optimized plan with `show_graph`.

=== ":fontawesome-brands-python: Python"
    ``` python
    --8<-- "user-guide/python/lazy/query_plan.py:show"
    ```

![](../../src/images//query_plan_optimized.png)

We can also print the optimized plan with `describe_optimized_plan`

=== ":fontawesome-brands-python: Python"
    ``` python
    --8<-- "user-guide/python/lazy/query_plan.py:optimized"
    ```

```text
 WITH_COLUMNS:
 [col("name").str.uppercase()]

    CSV SCAN data/reddit.csv
    PROJECT */6 COLUMNS
    SELECTION: [(col("comment_karma")) > (0)]
```

The optimized plan is to:

- read the data from the Reddit CSV
- apply the filter on the `comment_karma` column while the CSV is being read line-by-line
- transform the `name` column to uppercase

In this case the query optimizer has identified that the `filter` can be applied while the CSV is read from disk rather than writing the whole file to disk and then applying it. This optimization is called *Predicate Pushdown*.