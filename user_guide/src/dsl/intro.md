# Polars Expressions

Polars has a powerful concept called expressions. Polars expressions can be used in
various context and produce Series. That may sound a bit strange, so lets give an
example.

The following is an expression:

`col("foo").sort().head(2)`

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

### count unique values

We can count the unique values in a column. Note that we are creating the same result in
a different ways. To not have duplicate column names in the `DataFrame`, we use an
`alias` expression, which renames an expression.

```python
{{#include ../examples/expressions/expressions_examples_1.py:5:}}
print(df)
```

```text
{{#include ../outputs/expressions/example_1.txt}}
```

### various aggregations

We can do various aggregations. Below we show some of them, but there are more, such as
`median`, `mean`, `first` etc.

```python
{{#include ../examples/expressions/expressions_examples_2.py:5:}}
print(df)
```

```text
{{#include ../outputs/expressions/example_2.txt}}
```

### filter and conditionals

We can also do quite some complex things. In the next snippet we count all names ending
with the string `"am"`.

```python
{{#include ../examples/expressions/expressions_examples_3.py:5:}}
print(df)
```

```text
{{#include ../outputs/expressions/example_3.txt}}
```

### Binary functions and modification

In the example below we use a conditional to create a new expression in the following
`when -> then -> otherwise` construct. The `when()` function requires a predicate
expression (and thus leads to a `boolean` `Series`), the `then` requires expects an
expression that will be used in case the predicate evaluates `true`, and the `otherwise`
expects and expression that will be used in case the predicate evaluates `false`.

Note that you can pass any expression, or just base expressions like `col("foo")`,
`lit(3)`, `lit("bar")`, etc.

Finally, we multiply this with result of a sum expression.

```python
{{#include ../examples/expressions/expressions_examples_4.py:5:}}
print(df)
```

```text
{{#include ../outputs/expressions/example_4.txt}}
```

This is only, a small tip of the possible expressions, there are a ton more, and they
can be combined myriad ways.

This page was an introduction to Polars expressions and gave a glimpse of what's
possible with them. Next page we see in which contexts we can use expressions. And later we'll go through expressions
in various groupby contexts and by doing that keep Polars execution parallel.
