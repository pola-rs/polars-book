# Polars Expressions

The following is an expression:

`pl.col("foo").sort().head(2)`

The snippet above says:

1. Select column "foo"
1. Then sort the column
1. Then take the first two values of the sorted output

The power of expressions is that every expression produces a new expression, and that they
can be *piped* together. You can run an expression by passing them to one of `Polars` execution contexts.

Here we run two expressions by running `df.select`:

```python
df.select([
    pl.col("foo").sort().head(2),
    pl.col("bar").filter(pl.col("foo") == 1).sum()
])
```

All expressions are ran in parallel, meaning that separate `Polars` expressions are **embarrassingly
parallel**. Note that within an expression there may be more parallelization going on.

## Expression examples

In this section we will go through some examples, but first let's create a dataset:

```python
{{#include ../examples/expressions/dataset.py}}
print(df)
```

```text
{{#include ../outputs/expressions/dataset.txt}}
```

You can do a lot with expressions. They are so expressive that you sometimes have
multiple ways to get the same results. To get a better feel for them let's go through some
more examples.

### Count unique values

We can count the unique values in a column. Note that we are creating the same result in
different ways. To avoid duplicate column names in the `DataFrame`, we could use an
`alias` expression that can rename the expression.

```python
{{#include ../examples/expressions/expressions_examples_1.py:4:}}
print(out)
```

```text
{{#include ../outputs/expressions/example_1.txt}}
```

### Various aggregations

We can do various aggregations. Below are examples of some of them, but there are more such as
`median`, `mean`, `first`, etc.

```python
{{#include ../examples/expressions/expressions_examples_2.py:4:}}
print(out)
```

```text
{{#include ../outputs/expressions/example_2.txt}}
```

### Filter and conditionals

We can also do some pretty complex things. In the next snippet we count all names ending
with the string `"am"`.

```python
{{#include ../examples/expressions/expressions_examples_3.py:4:}}
print(df)
```

```text
{{#include ../outputs/expressions/example_3.txt}}
```

### Binary functions and modification

In the example below we use a conditional to create a new expression in the following
`when -> then -> otherwise` construct. The `when` function requires a predicate
expression (and thus leads to a boolean `Series`). The `then` function expects an
expression that will be used in case the predicate evaluates to `true`, and the `otherwise`
function expects an expression that will be used in case the predicate evaluates to `false`.

Note that you can pass any expression, or just base expressions like `pl.col("foo")`,
`pl.lit(3)`, `pl.lit("bar")`, etc.

Finally, we multiply this with the result of a `sum` expression:

```python
{{#include ../examples/expressions/expressions_examples_4.py:4:}}
print(df)
```

```text
{{#include ../outputs/expressions/example_4.txt}}
```

### Window expressions

A polars expression can also do an implicit GROUPBY, AGGREGATION, and JOIN in a single expression.
In the examples below we do a GROUPBY OVER `"groups"` and AGGREGATE SUM of `"random"`, and in the next expression
we GROUPBY OVER `"names"` and AGGREGATE a LIST of `"random"`. These window functions can be combined with other expressions
and are an efficient way to determine group statistics. See more on those group statistics [here](POLARS_PY_REF_GUIDE/expression.html#aggregation).

```python
{{#include ../examples/expressions/window.py:4:}}
print(df)
```

```text
{{#include ../outputs/expressions/window_0.txt}}
```

## Conclusion

This is the tip of the iceberg in terms of possible expressions. There are a ton more, and they
can be combined in a variety ways.

This page was an introduction to `Polars` expressions, and gave a glimpse of what's
possible with them. In the next page we'll discuss in which contexts expressions can be used. Later in the guide we'll go through expressions in various groupby contexts, all while keeping `Polars` execution parallel.
