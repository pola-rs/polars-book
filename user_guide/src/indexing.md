# Selecting data

In this page we show how to select rows and/or columns from a `DataFrame` or rows from a `Series`.  Understanding the key concepts here is perhaps the simplest way to start with the Expression API.

For simplicity we deal with `DataFrame` examples throughout. The principles are the same for `Series` objects except that columns obviously cannot be selected in a `Series`.

## Indexing with square brackets and selecting data with the Expression API

There are two ways to select rows and/or columns from a `DataFrame`:

- indexing with square brackets
- using the Expression API via the `filter` or `select` methods

To illustrate both of these methods we define a simple `DataFrame`:

```python
{{#include examples/selecting_data/indexing_selecting_examples.py:4:10}}
print(df)
```

```text
{{#include outputs/selecting_data/simple_df.txt}}
```

We want to select all rows with `id` less than or equal to 2 along with the `id` and `color` columns. With indexing we can do this as follows:

```python
{{#include examples/selecting_data/indexing_selecting_examples.py:12:12}}
print(indexing_df)
```

```text
{{#include outputs/selecting_data/indexing_df.txt}}
```

and with the Expression API we can do this as follows:

```python
{{#include examples/selecting_data/indexing_selecting_examples.py:14:14}}
print(indexing_df)
```

```text
{{#include outputs/selecting_data/expression_df.txt}}
```

We strongly recommend that you use the Expression API approach wherever possible:

- the indexing approach does not work in lazy mode and cannot be optimized
- the Expression API approach can be parallelized in eager and lazy mode

The `Polars` `DataFrame` doesn't have an index, therefore indexing behavior can be consistent without the need of a `df.loc`,
`df.iloc`, or a `df.at` operation.

The rules are as follows (depending on the datatypes of the values):

- **numeric**

  - axis 0: row
  - axis 1: column

- **numeric + strings**

  - axis 0: row (only accept numbers here)
  - axis 1: column (accept numeric + string values)

- **only strings**

  - axis 0: column
  - axis 1: error

- **expressions**

  _All expression evaluations are executed in parallel_

  - axis 0: column
  - axis 1: column
  - ..
  - axis n: column

## Comparison with pandas

| pandas                                                                | polars                        |
|-----------------------------------------------------------------------|-------------------------------|
| select row<br> `df.iloc[2]`                                           | `df[2, :]`                    |
| select several rows by their indices<br> `df.iloc[[2, 5, 6]]`         | `df[[2, 5, 6], :]`            |
| select slice of rows<br> `df.iloc[2:6]`                               | `df[2:6, :]`                  |
| select rows using a boolean mask<br> `df.iloc[True, True, False]`     | `df[[True, True, False]]`     |
| select rows by a predicate condition<br> `df.loc[df["A"] > 3]`        | `df[df["A"] > 3]`             |
| select slice of columns<br> `df.iloc[:, 1:3]`                         | `df[:, 1:3]`                  |
| select slice of columns by string order<br> `df.loc[:, "A":"Z"]`      | `df[:, "A":"Z"]`              |
| select a single value (scalar)<br> `df.loc[2, "A"]`                   | `df[2, "A"]`                  |
| select a single value (scalar)<br> `df.iloc[2, 1]`                    | `df[2, 1]`                    |
| select a single value (Series/DataFrame)<br> `df.loc[2, ["A"]]`       | `df[2, ["A"]]`                |
| select a single value (Series/DataFrame)<br> `df.iloc[2, [1]]`        | `df[2, [1]]`                  |

## Anti-pattern

Indexing polars by boolean masks is considered an anti-pattern and the functionality may be removed in the future.
Polars strongly favours the expression API in combination with `select` and `filter` in favor of accessing by index.
