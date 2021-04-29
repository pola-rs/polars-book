# Other optimizations
Besides predicate and projection pushdown, Polars does other optimizations.

One important one is optional caching and parallelization. One can imagine having two different DataFrame computations that
lead to a scan of the same file. Polars may cache the scanned file to prevent scanning the same file twice. However, if 
you want to, you may override this behavior and force polars to read the same file. This could
be faster because the scan could be done in parallel.

## Join parallelization
If we look at the previous query, we see that the join operation has as input a computation path with `data/reddit.csv`
as root and one path with `data/runescape.csv` as root. Polars can observe that there are no dependencies between the
two DataFrame and will read both files in parallel. If other operations are done before the join (e.g. groupby, filters, etc.)
they are also executed in parallel.

![query_plan_opt](../img/projection_pushdown_0_optimized.png)

## Simplify expressions
Some other optimizations that are done are expression simplifications. The impact of these optimizations is less than that
of predicate and projection pushdown, but they likely add up. You can [track this issue](https://github.com/ritchie46/polars/issues/139)
to see the latest status of those.
