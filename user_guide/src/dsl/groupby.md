# GroupBy

> The GroupBy page is under construction.

## A multithreaded approach

One of the most efficient ways to process tabular data is to parallelize its processing
via the "split-apply-combine" approach. This operation is at the core of the `Polars`
grouping implementation, allowing it to attain lightning-fast operations. Specifically, both the "split" and "apply" phases are executed in a multi-threaded
fashion.

A simple grouping operation is taken below as an example to illustrate this approach:

![](https://raw.githubusercontent.com/pola-rs/polars-static/master/docs/split-apply-combine.svg)

For the hashing operations performed during the "split" phase, `Polars` uses a
multithreaded lock-free approach that is illustrated on the following schema:

![](https://raw.githubusercontent.com/pola-rs/polars-static/master/docs/lock-free-hash.svg)

This parallelization allows the grouping and joining operations (for instance) to be
blazingly fast!

> Check out [this blog post](https://www.ritchievink.com/blog/2021/02/28/i-wrote-one-of-the-fastest-dataframe-libraries/)
> for more details.

## Do not kill the parallelization!

We have all heard that `Python` is slow, and does "not scale." Besides the overhead of
running "slow" bytecode, `Python` has to remain within the constraints of the Global
Interpreter Lock (GIL). This means that if you were to use a `lambda` or a custom `Python`
function to apply during a parallelized phase, `Polars` speed is capped running `Python`
code preventing any multiple threads from executing the function.

This all feels terribly limiting, especially because we often need those `lambda` functions in a
`.groupby()` step, for example. This approach is still supported by `Polars`, but
keeping in mind bytecode **and** the GIL costs have to be paid.

To mitigate this, `Polars` implements a powerful syntax defined not only in its lazy API,
but also in its eager API.

## Polars Expressions

In the introduction on the previous page we discussed that using custom Python functions,
killed parallelization, and that we can use the expressions of the lazy API to mitigate
this. Let's take a look at what that means.

We can start with the simple
[US congress dataset](https://github.com/unitedstates/congress-legislators).

```python
{{#include ../examples/groupby_dsl/snippet1.py}}
```

#### Basic aggregations

You can easily combine different aggregations by adding multiple expressions in a
`list`. There is no upper bound on the number of aggregations you can do, and you can
make any combination you want. In the snippet below we do the following aggregations:

Per GROUP `"first_name"` we

- count the number of rows in the group:
  - short form: `pl.count("party")`
  - full form: `pl.col("party").count()`
- aggregate the gender values groups to a list:
  - full form: `pl.col("gender").list()`
- get the first value of column `"last_name"` in the group:
  - short form: `pl.first("last_name")`
  - full form: `pl.col("last_name").first()`

Besides the aggregation, we immediately sort the result and limit to the top `5` so that
we have a nice summary overview.

```python
{{#include ../examples/groupby_dsl/snippet1.py}}
```

```text
{{#include ../outputs/groupby_dsl/output1.txt}}
```

#### Conditionals

It's that easy! Let's turn it up a notch. Let's say we want to know how
many delegates of a "state" are "Pro" or "Anti" administration. We could directly query
that in the aggregation without the need of `lambda` or grooming the `DataFrame`.

```python
{{#include ../examples/groupby_dsl/snippet2.py}}
```

```text
{{#include ../outputs/groupby_dsl/output2.txt}}
```

Similarly,  this could also be done with a nested GROUPBY, but that doesn't help show off some of these nice features. 😉

```python
{{#include ../examples/groupby_dsl/snippet3.py}}
```

```text
{{#include ../outputs/groupby_dsl/output3.txt}}
```

#### Filtering

We can also filter the groups. Let's say we want to compute a mean per group, but we
don't want to include all values from that group, and we also don't want to filter the
rows from the `DataFrame` (because we need those rows for another aggregation).

In the example below we show how that can be done. Note that we can make `Python`
functions for clarity. These functions don't cost us anything. That is because we only
create `Polars` expressions, we don't apply a custom function over a `Series` during
runtime of the query.

```python
{{#include ../examples/groupby_dsl/snippet4.py}}
```

```text
{{#include ../outputs/groupby_dsl/output4.txt}}
```

#### Sorting

It's common to see a `DataFrame` being sorted for the sole purpose of managing the ordering during a
GROUPBY operation. Let's say that we want to get the names of the oldest and youngest politicians per state. We could SORT and GROUPBY.

```python
{{#include ../examples/groupby_dsl/snippet5.py}}
```

```text
{{#include ../outputs/groupby_dsl/output5.txt}}
```

However, **if** we also want to sort the names alphabetically, this
breaks. Luckily we can sort in a `groupby` context separate from the `DataFrame`.

```python
{{#include ../examples/groupby_dsl/snippet6.py}}
```

```text
{{#include ../outputs/groupby_dsl/output6.txt}}
```

We can even sort by another column in the `groupby` context. If we want to know if the
alphabetically sorted name is male or female we could add:
`pl.col("gender").sort_by("first_name").first().alias("gender")`

```python
{{#include ../examples/groupby_dsl/snippet7.py}}
```

```text
{{#include ../outputs/groupby_dsl/output7.txt}}
```

### Conclusion

In the examples above we've seen that we can do a lot by combining expressions. By doing
so we delay the use of custom `Python` functions that slow down the queries (by the slow
nature of Python AND the GIL).

If we are missing a type expression let us know by opening a
[feature request](https://github.com/pola-rs/polars/issues/new/choose)!
