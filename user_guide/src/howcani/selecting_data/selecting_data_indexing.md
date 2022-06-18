# Selecting with indexing

In this page we cover use of square bracket indexing to select data. Square bracket indexing
can be used to select rows and/or columns.

## Indexing is an anti-pattern in `Polars`

Indexing polars with square brackets is considered an anti-pattern and the functionality may be removed in the future.
Polars [strongly favours the expression API with `select` and `filter`](selecting_data_expressions.md) in favor of accessing by square bracket indexing. See the [introduction to this section](selecting_data_intro.md) for more information.

## Indexing does not work in lazy mode

Selecting data by indexing only works with a `DataFrame` in eager mode. If you try to select data by indexing on a `LazyFrame` it will raise an exception that a `LazyFrame` is not subscriptable. Instead you need to [select data using expressions](selecting_data_expressions.md).

## Rules for square bracket indexing

The rules for square bracket indexing are as follows (depending on the datatypes of the values):

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
