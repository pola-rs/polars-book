# Predicate pushdown

> The Predicate pushdown page is under construction

Predicate pushdown is an optimization `Polars` does that reduces query times and memory
usage. A predicate is database jargon for applying a filter on some table, thereby
reducing the number of rows on that table.

So let's see if we can load some Reddit data and filter on a few predicates.

```python
{{#include ../../examples/predicate_pushdown/snippet1.py}}
```

If we were to run this query above nothing would happen! This is due to the lazy evaluation.
Nothing will happen until specifically requested. This allows Polars to see the whole
context of a query and optimize just in time for execution.

Execution is requested by the `.collect` method. This would query all available data.
While you're writing, optimizing, and checking your query, this is often undesirable. Another
method that calls for execution is the `.fetch` method. `.fetch` takes a parameter
`n_rows` and tries to 'fetch' that number of rows at the data source (no guarantees are
given though).

So let's "fetch" ~10 Million rows from the source file and apply the predicates.

```python
q1.fetch(n_rows=int(1e7))
```

```text
{{#include ../../outputs/predicate_pushdown/output1.txt}}
```

Above we see that from the 10 Million rows, 61503 rows match our predicate.

## Break it down

In `Polars` we can visualize the query plan. Let's take a look.

```python
q1.show_graph(optimized=False)
```

![](../../outputs/predicate_pushdown/graph1.png)

The astute reader maybe would notice that our query is not very optimal because we have
three separate *FILTER* nodes. That means that after every *FILTER* a new `DataFrame` is
allocated, which will be input to the next *FILTER* and then deleted from memory -- that
must be redundant, and you know what... they'd be right. The predicates should be
combined. We should have written this query:

```python
{{#include ../../examples/predicate_pushdown/snippet2.py}}
```

That would translate to:

```python
q2.show_graph(optimized=False)
```

![](../../outputs/predicate_pushdown/graph2.png)

As we can see the predicates are combined. This would lead to less copying of data.

## In comes optimization

`Polars` tries to save that mental overhead from the query writer and combines predicates
for you. Besides that, it pushes predicates down to the scan level! Let's see how our
optimized query looks.

```python
q1.show_graph(optimized=True)
```

![](../../outputs/predicate_pushdown/graph1-optimized.png)

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
