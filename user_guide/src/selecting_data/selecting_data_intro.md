# Selecting data

In this section we show how to select rows and/or columns from a `DataFrame` or rows from a `Series`.  Understanding the key concepts here is perhaps the simplest way to get started with the Expression API.

For simplicity we deal with `DataFrame` examples throughout. The principles are the same for `Series` objects except that columns obviously cannot be selected in a `Series`.

In this page we introduce the two approaches for selecting data and the reasons why the expression approach is favoured. In subsequent pages we cover:

- [Selecting data with expressions](selecting_data_expressions.md)
- [Selecting data with indexing](selecting_data_indexing.md)

## Example of selecting data

There are two ways to select rows and/or columns from a `DataFrame`:

- indexing with square brackets
- using the Expression API via the `filter` or `select` methods

To illustrate both of these methods we define a simple `DataFrame`:

```python
{{#include ../examples/selecting_data/indexing_selecting_examples.py:4:10}}
print(df)
```

```text
{{#include ../outputs/selecting_data/simple_df.txt}}
```

We want to select all rows with `id` less than or equal to 2 along with the `id` and `color` columns. With indexing we can do this as follows:

```python
{{#include ../examples/selecting_data/indexing_selecting_examples.py:12:12}}
print(indexing_df)
```

```text
{{#include ../outputs/selecting_data/indexing_df.txt}}
```

and with the Expression API we can do this as follows:

```python
{{#include ../examples/selecting_data/indexing_selecting_examples.py:14:14}}
print(indexing_df)
```

```text
{{#include ../outputs/selecting_data/expression_df.txt}}
```

The use case for indexing is for exploratory data analysis when you want to look at a subset of data. We **strongly recommend** using the Expression API approach for all other use cases. This is because:

- the indexing approach does not work in lazy mode and cannot be optimized
- the Expression API approach can be parallelized in eager and lazy mode
