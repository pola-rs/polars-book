# List context

An expression context we haven't discussed yet is the `List` context. This means simply we can apply any expression on the elements of a `List`.

> A note for `Rust` users, these features require the `list` feature flag.

# Row wise computations

This context is ideal for computing things in row orientation.

Polars expressions work on columns that have the guarantee that they consist of homogeneous data.
Columns have this guarantee, rows in a `DataFrame` not so much.
Luckily we have a data type that has the guarantee that the rows are homogeneous: `pl.List` data type.

Let's say we have the following data:

<div class="tabbed-blocks">

```python
{{#include ../examples/expressions/list_row_wise_1.py:3:}}
print(grades)
```

```rust,noplayground
{{#include ../examples/expressions/list_row_wise.rs:dataset}}
```

</div>

```text
{{#include ../outputs/expressions/list_row_wise_1.txt}}
```

If we want to compute the `rank` of all the columns except for `"student"`, we can collect those into a `list` data type:

This would give:

<div class="tabbed-blocks">

```python
{{#include ../examples/expressions/list_row_wise_2.py:4:}}
print(out)
```

```rust,noplayground
{{#include ../examples/expressions/list_row_wise.rs:row-wise}}
```

</div>

```text
{{#include ../outputs/expressions/list_row_wise_2.txt}}
```

## Running polars expression on list elements

We can run **any** polars expression on the elements of a list with the `arr.eval` (`arr().eval` in Rust) expression! These expressions run entirely on polars' query engine and can run in parallel so will be super fast.

Let's expand the example from above with something a little more interesting. Pandas allows you to compute the percentages of the `rank` values. Polars doesn't provide such a keyword argument. But because expressions are so versatile we can create our own percentage rank expression. Let's try that!

Note that we must `select` the list's element from the context. When we apply expressions over list elements, we use `pl.element()` to select the element of a list.

> Also note that to use `arr().eval` in Rust requires the `list_eval` feature flag.

<div class="tabbed-blocks">

```python
# the percentage rank expression
rank_pct = pl.element().rank(descending=True) / pl.col("").count()


grades.with_columns(
    # create the list of homogeneous data
    pl.concat_list(pl.all().exclude("student")).alias("all_grades")
).select([
    # select all columns except the intermediate list
    pl.all().exclude("all_grades"),
    # compute the rank by calling `arr.eval`
    pl.col("all_grades").arr.eval(rank_pct, parallel=True).alias("grades_rank")
])
```

```rust,noplayground
{{#include ../examples/expressions/list_row_wise.rs:expressions}}
```

</div>

This outputs:

```
shape: (4, 5)
┌─────────┬────────────┬─────────┬───────────┬────────────────────────────────┐
│ student ┆ arithmetic ┆ biology ┆ geography ┆ grades_rank                    │
│ ---     ┆ ---        ┆ ---     ┆ ---       ┆ ---                            │
│ str     ┆ i64        ┆ i64     ┆ i64       ┆ list [f32]                     │
╞═════════╪════════════╪═════════╪═══════════╪════════════════════════════════╡
│ bas     ┆ 10         ┆ 4       ┆ 8         ┆ [0.333333, 1.0, 0.666667]      │
├╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┤
│ laura   ┆ 5          ┆ 6       ┆ 4         ┆ [0.666667, 0.333333, 1.0]      │
├╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┤
│ tim     ┆ 6          ┆ 2       ┆ 9         ┆ [0.666667, 1.0, 0.333333]      │
├╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┤
│ jenny   ┆ 8          ┆ 7       ┆ 7         ┆ [0.333333, 0.833333, 0.833333] │
└─────────┴────────────┴─────────┴───────────┴────────────────────────────────┘

```

Note that this solution works for any expressions/operation you want to do row wise.
