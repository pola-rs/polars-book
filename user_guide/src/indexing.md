# Selecting data

In this page we show how to select rows and/or columns from a `DataFrame` or rows from a `Series`. In doing so we show how to use the `Polars` Expression API that is key to achieving high performance. Understanding the key concepts here is perhaps the simplest way to start with the Expression API.

For simplicity we deal with `DataFrame` examples throughout. The principles are the same for `Series` objects except that columns obviously cannot be selected in a `Series`.

## Indexing with square brackets and selecting data with the Expression API
There are two ways to select rows and/or columns from a `DataFrame`:
- indexing with square brackets
- using the Expression API via the `filter` or `select` methods



We strongly recommend that you use the Expression API approach whereever possible:
- the indexing approach does not work in lazy mode
- the Expression API approach can be parallelized


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
