# Polars Expressions

Polars has a powerful concept called expressions. Polars expressions can be used in
various contexts and produce Series. That may sound a bit strange, so lets give an
example.

The following is an expression:

`pl.col("foo").sort().head(2)`

The snippet above says on `select column "foo" -> sort -> take first 2 values`. The
power of expressions is that every expression produces a new expression and that they
can be `piped` together. Besides, being very expressive, they are also **embarrassingly
parallel**!

## Expression examples

In the next section we will go through some examples, but first create a dataset:

```python
{{#include ../examples/expressions/dataset.py}}
print(df)
```

```text
{{#include ../outputs/expressions/dataset.txt}}
```

## Some more examples.

You can do a lot with expressions. They are so expressive that you sometimes have got
multiple ways to get the same results. To get a feel for them let's go through some
examples.

### Count unique values

We can count the unique values in a column. Note that we are creating the same result in
different ways. To not have duplicate column names in the `DataFrame`, we use an
`alias` expression, which renames an expression.

```python
{{#include ../examples/expressions/expressions_examples_1.py:4:}}
print(df)
```

```text
{{#include ../outputs/expressions/example_1.txt}}
```

### Various aggregations

We can do various aggregations. Below we show some of them, but there are more, such as
`median`, `mean`, `first` etc.

```python
{{#include ../examples/expressions/expressions_examples_2.py:4:}}
print(df)
```

```text
{{#include ../outputs/expressions/example_2.txt}}
```

### Filter and conditionals

We can also do quite some complex things. In the next snippet we count all names ending
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
`when -> then -> otherwise` construct. The `when()` function requires a predicate
expression (and thus leads to a `boolean` `Series`), the `then` expects an
expression that will be used in case the predicate evaluates `true`, and the `otherwise`
expects an expression that will be used in case the predicate evaluates `false`.

Note that you can pass any expression, or just base expressions like `pl.col("foo")`,
`pl.lit(3)`, `pl.lit("bar")`, etc.

Finally, we multiply this with result of a sum expression.

```python
{{#include ../examples/expressions/expressions_examples_4.py:4:}}
print(df)
```

```text
{{#include ../outputs/expressions/example_4.txt}}
```

### Window expressions (split-apply-combine)

A polars expression can also do an implicit GROUPBY, AGGREGATION, and JOIN in a single expression.
In the examples below we do a GROUPBY OVER `"groups"` and AGGREGATE SUM of `"random"`, and in the next expression
we GROUPBY OVER `"names"` and AGGREGATE a LIST of `"random"`. These window functions can be combined with other expressions,
and are an efficient way to determine group statistics. See more of those [group statistics here](POLARS_PY_REF_GUIDE/expression.html#aggregation)

```python
{{#include ../examples/expressions/window.py:4:}}
print(df)
```

```text
{{#include ../outputs/expressions/window_0.txt}}
```

## Conclusion

This is only, a small tip of the possible expressions, there are a ton more, and they
can be combined in myriad ways.

This page was an introduction to Polars expressions and gave a glimpse of what's
possible with them. In the next page we see in which contexts we can use expressions. And later we'll go through expressions
in various groupby contexts and by doing that keep Polars execution parallel.
