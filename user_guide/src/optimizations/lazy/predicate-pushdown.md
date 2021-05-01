# Predicate pushdown

> In redaction

Predicate pushdown is an optimization Polars does that reduces query times and memory
usage. A predicate is database jargon for applying a filter on some table and thereby
reducing number the number of rows on that table.

So let's see if we can load some Reddit data and filter on a few predicates.

```python
{{#include ../../_examples/predicate-pushdown/snippet1.py}}
```

If we were to run this query above, nothing would happen! This due to the lazyness,
nothing will happend until specifically requested. This allows Polars to see the whole
context of a query and optimize just in time for execution.

Execution is requested by the `.collect` method. This would query all available data.
During writing/ optimizing/ checking your query this is often not what you want. Another
method that calls for execution is the `.fetch` method. `.fetch` takes a parameter
`n_rows` and tries to 'fetch' that number of rows at the data source (no guarantees are
given though).

So let's "fetch" ~10 Million rows from the source file and apply the predicates.

```python
reddit.fetch(n_rows=int(1e7))
```

```text
{{#include ../../_outputs/predicate-pushdown/output1.txt}}
```

Above we see that from the 10 Million rows, 61503 rows match our predicate.

## Break it down

In Polars we can visualize the query plan. Let's take a look.

```python
reddit.show_graph(optimized=False)
```

![](../../_outputs/predicate-pushdown/graph1.png)

The astute reader maybe would notice that our query is not very optimal because we have
3 separate *FILTER* nodes. That means that after every *FILTER* a new DataFrame is
allocated, which will be input to the next *FILTER* and then deleted from memory, that
must be redundant. And you know what.. He/she is right, the predicates should be
combined, we should have written this query:

```python
{{#include ../../_examples/predicate-pushdown/snippet2.py}}
```

That would translate to:

```python
reddit_2.show_graph(optimized=False)
```

![](../../_outputs/predicate-pushdown/graph2.png)

As we can see the predicates are combined. This would lead to less copying of data

## In comes optimization

Polars tries to save that mental overhead from the query writer and combines predicates
for you. Besides that, it pushes predicates down to the scan level! Let's see how our
optimized query looks.

```python
reddit.show_graph(optimized=True)
```

![](../../_outputs/predicate-pushdown/graph1-optimized.png)

It may be hard to see, but what is clear is that there is only a single node; the *CSV
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

**with optimization**, `predicate_pushdown=True` flag:

```text
real	0m1,597s
user	0m6,143s
sys	0m0,647s
```

## Relational algebra

In the visualization of the query plan, you see a \\( \\sigma \\) symbol. This indicates
a Predicate done at the *SCAN* level. There is also a \\( \\pi \\) symbol indicating
projection (database jargon for column selection), but we'll get to that later.

## Cheaper joins

Predicate pushdown optimization will generally also lead to cheaper join's. A join is
quite an expensive operation the less rows we through at a join operation, the cheaper
it becomes.
