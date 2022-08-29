# Expression contexts

You cannot use an expression anywhere. An expression needs a context, the available contexts are:

- selection: `df.select([..])`
- groupy aggregation: `df.groupby(..).agg([..])`
- hstack/ add columns: `df.with_columns([..])`

## Syntactic sugar

The reason for such a context, is that you actually are using the Polars lazy API, even if you use it in eager.
For instance this snippet:

<div class="tabbed-blocks">

```python
df.groupby("foo").agg([pl.col("bar").sum()])
```

```rust,noplayground
eager.groupby(["foo"])?.agg(&[("bar", &["sum"])])?;
```

</div>

actually desugars to:

<div class="tabbed-blocks">

```python
(df.lazy().groupby("foo").agg([pl.col("bar").sum()])).collect()
```

```rust,noplayground
eager.lazy().groupby(["foo"]).agg([col("bar").sum()]).collect()?;
```

</div>

This allows Polars to push the expression into the query engine, do optimizations, and cache intermediate results.

Rust differes from Python somewhat in this respect.  Where Python's eager mode is little more than a thin veneer over the lazy API, Rust's eager mode is closer to an implementation detail, and isn't really recommended for end-user use.  It is possible that the eager API in Rust will be scoped private sometime in the future.  Therefore, for the remainder of this document, assume that the Rust examples are using the lazy API.

## Select context

In the `select` context the selection applies expressions over columns. The expressions in this context must produce `Series` that are all
the same length or have a length of `1`.

A `Series` of a length of `1` will be broadcasted to match the height of the `DataFrame`.
Note that a `select` may produce new columns that are aggregations, combinations of expressions, or literals.

#### Selection context

<div class="tabbed-blocks">

```python
{{#include ../examples/expressions/select_context_2.py:4:}}
print(out)
```

```rust,noplayground
{{#include ../examples/expressions/contexts.rs:select}}
```

</div>

```text
{{#include ../outputs/expressions/select_context_2.txt}}
```

**Add columns**

Adding columns to a `DataFrame` using `with_columns` is also the `selection` context.

<div class="tabbed-blocks">

```python
{{#include ../examples/expressions/with_column_context_1.py:4:}}
print(df)
```

```rust,noplayground
{{#include ../examples/expressions/contexts.rs:add_columns}}
```

</div>

```text
{{#include ../outputs/expressions/wc_context_1.txt}}
```

## Groupby context

In the `groupby` context expressions work on groups and thus may yield results of any length (a group may have many members).

<div class="tabbed-blocks">

```python
{{#include ../examples/expressions/agg_context_1.py:4:}}
print(out)
```

```rust,noplayground
{{#include ../examples/expressions/contexts.rs:groupby}}
```

</div>

```text
{{#include ../outputs/expressions/agg_context_1.txt}}
```

Besides the standard `groupby`, `groupby_dynamic`, and `groupby_rolling` are also entrances to the `groupby context`.
