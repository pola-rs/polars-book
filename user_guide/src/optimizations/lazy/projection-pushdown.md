# Projection pushdown

> The Projection pushdown page is under construction.

Let's expand our query from the previous section by joining the result of the *FILTER*
operation with the runescape data to find popular Reddit usernames that have a
username starting with an `"a"` that also played Runescape. That must be something we are all
interested in!

The query would look like this:

```python
{{#include ../../examples/projection_pushdown/snippet.py}}
```

And yields the following DataFrame.

```text
{{#include ../../outputs/projection_pushdown/output.txt}}
```

## Break it down

Again, let's take a look the query plan.

```python
dataset.show_graph(optimized=False)
```

![](./../outputs/projection_pushdown/graph.png)

Now were focussed on the projection's indicated with π. The first node shows π 3/6,
indicating that we select 3 out of 6 columns in the `DataFrame`. If we look the csv scans
we see a wildcard π \*/6 and π \*/1 meaning that we select all of 6 columns of the
reddit dataset and the one and only column from the runescape dataset respectively.

This query is not very optimal. We select all columns from both datasets and only show
3/6 after join. That means that there were some columns computed during the join
operation that could have been ignored. There were also columns parsed during csv
scanning only to be dropped at the end. When we are dealing with `DataFrame`s with a
large number of columns the redundant work that is done can be huge.

### Optimized query

Let's see how `Polars` optimizes this query.

```python
dataset.show_graph(optimized=True)
```

![](./../outputs/projection_pushdown/graph-optimized.png)

The projections are pushed down the join operation all the way to the csv scans. This
means that both the scanning and join operation have become cheaper due to the query
optimization.

## Performance

Let's time the result before and after optimization.

**Without optimization**, `predicate_pushdown=False` and `projection_pushdown=False`.

```text
real	0m3,273s
user	0m9,284s
sys	0m1,081s
```

**With optimization**, `predicate_pushdown` and `projection_pushdown` flags both to
`True`.

```text
real	0m1,732s
user	0m7,581s
sys	0m0,783s
```

We can see that we almost reduced query time by half on this simple query. With real
business data often comprising of many columns, filtering missing data, doing complex
groupby operations, and using joins we expect this difference between unoptimized queries and optimized
queries to only grow.
