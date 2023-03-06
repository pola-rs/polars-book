# Predicate pushdown

A *predicate* is database jargon for applying a filter condition on some table, thereby reducing the number of rows from that table.

Predicate pushdown is an optimization `Polars` does that reduces query times and memory usage.

On the previous page we introduced our query where we load some Reddit data and filter on a few predicates

```python
{{#include ../../examples/predicate_pushdown/snippet1.py::10}}
```

Our query is not optimal because we have three separate *FILTER* nodes. That means that after every *FILTER* a new `DataFrame` is
allocated internally and this new `DataFrame` is input to the next *FILTER* and then deleted from memory. There is a lot of redundancy here.

We can manually combine the three predicates by writing this query with a single `filter` and the predicates combined with `&`:

```python
{{#include ../../examples/predicate_pushdown/snippet2.py::10}}
```

## Manual optimization

If we examine the query graph for this manually optimized query we get:

```python
q2.show_graph(optimized=False)
```

![](../../outputs/predicate_pushdown/graph2.png)

We can also print the plan (without Polars internal query optimization) with `describe_plan`

```python
{{#include ../../examples/predicate_pushdown/snippet2.py:10:10}}
```

```text
{{#include ../../outputs/predicate_pushdown/output8.txt}}
```

In this case the predicates are combined. This combination of predicates leads to less copying of data as Polars applies them all in a single pass over the same `DataFrame`.

## Automatic predicate combination

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

## Automatic predicate pushdown

However, Polars has done more than just combine the predicates. The Polars query optimiser does a *pushdown* to the scan level. This pushdown to the scan level means that the filters are applied as Polars reads the CSV file line-by-line. This is different to the manual optimization above where Polars reads the full CSV into memory before applying the filters. Let's see how our
optimized query looks.

It may be hard to see, but what is clear is that there is only a single node: the *CSV
SCAN*. The predicate filtering is done during the reading of the csv. This means that
this query's memory overhead is reduced by filtering factor! This makes a huge impact.

### Memory

As we have seen there were ~ 62,000 rows left after the *FILTER*. That means that (aside
for some memory overhead of the batch size and filter operations) we use \\(
\\frac{6.2\\text{e-}4}{1\\text{e-}7} \\sim 0.6 \\text{%} \\) of the memory we would
during an eager evaluation where we first would read the whole table in memory before
applying a filter.

### Performance

At the time of writing this, the predicate pushdown also increased the query time
performance.

**Without optimization**, `predicate_pushdown=False` flag:

```text
real	0m2,401s
user	0m5,457s
sys	0m0,894s
```

**With optimization**, `predicate_pushdown=True` flag:

```text
real	0m1,597s
user	0m6,143s
sys	0m0,647s
```

## Relational algebra

In the visualization of the query plan, you see a \\( \\sigma \\) symbol. This indicates
a predicate done at the *SCAN* level. There is also a \\( \\pi \\) symbol indicating
projection (database jargon for column selection), but we'll get to that later.

## Cheaper joins

Predicate pushdown optimization will generally also lead to cheaper join's. A join is
an expensive operation. The fewer rows we have in a join operation the cheaper
it will become.
