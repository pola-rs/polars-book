# GroupBy

> In redaction

## A multithreaded approach

One of the most efficient way to process tabular data is to parallelize its processing
via the "split-apply-combine" approach. This operation is at the core of `Polars`
grouping implementation, allowing it to attain lightning-fast operations. Most
specifically, both the "split" and "apply" phases are executed in a multithreaded
fashion.

A simple grouping operation is taken below as an example to illustrate this approach:

![](https://raw.githubusercontent.com/ritchie46/static/master/polars/split-apply-combine-par.svg)

For the hashing operations performed during the "split" phase, `Polars` uses a
multithreaded lock-free approach that can is illustrated on the following schema:

![](https://raw.githubusercontent.com/ritchie46/static/master/polars/lock-free-hash.svg)

This parallelization allows the grouping and joining operations (for instance) to be
blazingly fast!

> Include content from the
> [blog post](https://www.ritchievink.com/blog/2021/02/28/i-wrote-one-of-the-fastest-dataframe-libraries/)

## Do not kill the parallelization!

We have all heard that `Python` is slow, and does "not scale." Besides the overhead of
running "slow" bytecode, `Python` has to remain within the constraints of the Global
Interpreter Lock (GIL). This means that if one uses a `lambda` or a custom `Python`
function to apply during a parallelized phase, `Polars` speed is capped running `Python`
code preventing any multiple threads from executing the function.

This all feels terribly limiting, especially because we often need those `lambda` in a
`.groupby()` step for instance. This approach is still supported by `Polars`, but
keeping in mind bytecode AND the GIL price have to be paid.

To mitigate this, `Polars` implements a powerful syntax defined not only in its lazy,
but also in its eager API.

## Polars Expressions

In the introduction on previous page we discussed that using custom Python functions,
killed parallelization, and that we can use the expressions of the lazy API to mitigate
this. Let's take a look at what that means.

### Eager and Lazy

For groupby operations you can use the lazy API in Polars eager. That means that if you
run this snippet of code

```python
df.groupby("foo").agg([pl.col("bar").sum()])
```

It actually desugars to:

```python
(df.lazy().groupby("foo").agg([pl.col("bar").sum()])).collect()
```

That means you don't have to go to lazy by yourself if you need the more powerful API.

### Why would you want this.

As discussed earlier, this allows us to delay the need of grabbing Python `lambdas` to
do a more complex aggregation. So let's start very simple and see how we can use the DSL
to do increasingly complex queries.

Let's start with a simple dataset
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
  - full form: `col("party").count()`
- aggregate the gender values group to a list:
  - full form: `col("gender").list()`
- get the first value of column `"last_name"` in the group:
  - short form: `pl.first("last_name")`
  - full form: `col("last_name").first()`

Besides the aggregation, we immediately sort the result and limit to the top 5 so that
we have a nice summary overview.

```python
{{#include ../examples/groupby_dsl/snippet1.py}}
```

```text
{{#include ../outputs/groupby_dsl/output1.txt}}
```

#### Conditionals

Ok, that was pretty easy right. Let turn it up a notch. Let's say we want to know how
many delegates of a "state" are "Pro" or "Anti" administration we could directly query
that in the aggregation without the need of `lambda` or grooming the DataFrame.

```python
{{#include ../examples/groupby_dsl/snippet2.py}}
```

```text
{{#include ../outputs/groupby_dsl/output2.txt}}
```

Something similar could of course also be done with a nested GROUPBY, but that would not
allow me showing these nice features. 😉

```python
{{#include ../examples/groupby_dsl/snippet3.py}}
```

```text
{{#include ../outputs/groupby_dsl/output3.txt}}
```

#### Filtering

We can also filter the groups. Let's say we want to compute a mean per group, but we
don't want to include all values from that group and we also don't want to filter the
rows from the `DataFrame` (because we need that rows for another aggregation.)

In the example below we show how that can be done. Note that we can make `Python`
functions for clarity. These functions don't cost us anything. That is because we only
create `Polars` expression, we don't apply a custom function over `Series` during
runtime of the query.

```python
{{#include ../examples/groupby_dsl/snippet4.py}}
```

```text
{{#include ../outputs/groupby_dsl/output4.txt}}
```

#### Sorting

I often see a DataFrame being sorted for the sole purpose of the ordering during the
GROUPBY operation. Let's say that we want to get the names of the oldest and youngest
(not that they are still alive) politicians per state, we could SORT and GROUPBY.

```python
{{#include ../examples/groupby_dsl/snippet5.py}}
```

```text
{{#include ../outputs/groupby_dsl/output5.txt}}
```

However, IF we also want to sort the names alphabetically (and why wouldn't you!), this
breaks. Luckily we can sort in a groupby context separate from the `DataFrame`.

```python
{{#include ../examples/groupby_dsl/snippet6.py}}
```

```text
{{#include ../outputs/groupby_dsl/output6.txt}}
```

We can even sort by another column in the GROUPBY context. If we want to know if the
alphabetically sorted name is male or female we could add
`col("gender").sort_by("first_name").first().alias("gender")`

```python
{{#include ../examples/groupby_dsl/snippet7.py}}
```

```text
{{#include ../outputs/groupby_dsl/output7.txt}}
```

### Conclusion

In the examples above we've seen that we can do a lot by combining expressions. By doing
so we delay the use of custom python functions that slow down the queries (by the slow
nature of Python AND the GIL).

If you think there is a type expression missing, let me know and open a
[feature request](https://github.com/pola-rs/polars/issues/new/choose).
