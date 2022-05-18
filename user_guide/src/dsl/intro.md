# Polars Expressions

`Polars` has a powerful concept called expressions that is central to its very fast performance.  

Expressions are at the core of many data science operations:
- taking a sample of rows from a column
- multiplying values in a column
- extracting a column of years from dates
- convert a column of strings to lowercase
- and so on!

However, expressions are also used within other operations:
- taking the mean of a group in a `groupby` operation
- calculating the size of groups in a `groupby` operation
- taking the sum horizontally across columns

`Polars` performs these core data transformations very quickly by:
- automatic query optimization on each expression
- automatic parallelization of expressions on many columns

Polars expressions are a mapping from a series to a series (or mathematically `Fn(Series) -> Series`). As expressions have a `Series` as an input and a `Series` as an output then it is straightforward to do a sequence of expressions (similar to method chaining in `Pandas`).

This has all been a bit abstract, so let's start with some examples.
