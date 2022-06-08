# Selecting data

In this section we show how to select rows and/or columns from a `DataFrame` or rows from a `Series`.

The Expression API is one of the keys to writing performant queries. The simplest way to get started with the Expression API is to get familiar with the `filter` and `select` methods in this section.

The two approaches in this section are:

- [selecting data with expressions](selecting_data_expressions.md)
- [selecting data with square bracket indexing](selecting_data_indexing.md)

> Although they may give the same output, selecting data with expressions or square bracket indexing **are not equivalent**. The implementation of selecting data with expressions is totally different than the implementation of selecting data with square bracket indexing.

We **strongly recommend** selecting data with expressions for almost all use cases. Square bracket indexing is useful when doing exploratory data analysis in a terminal or notebook when you just want a quick look at a subset of data.

For all other use cases we recommend using expressions to select data because:

- expressions can be parallelized
- the expression approach can be used in lazy and eager mode while the indexing approach can only be used in eager mode
- in lazy mode the query optimizer can optimize expressions
