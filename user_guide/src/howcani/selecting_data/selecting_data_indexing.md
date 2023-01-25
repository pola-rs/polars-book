# Selecting with indexing

In this page we cover use of square bracket indexing to select data. Square bracket indexing can be used to select rows and/or columns.

## Indexing has a limited use case in `Polars`

There are some use cases in Polars where square bracket indexing is effective. However, there are many use cases where indexing prevents you from using the full power of Polars. 

Use cases where indexing **is** effective:
- to extract a scalar value from a `DataFrame`
- to convert a `DataFrame` column to a `Series`
- for exploratory data analysis and to inspect some rows and/or columns

The first downside of indexing with square brackets is that indexing only works in eager mode. Any steps in your query that involve square bracket indexing cannot be included in a lazy query meaning that the step cannot be optimised as part of a lazy query and the step cannot be part of a streaming query that processes larger-than-memory data in batches

The second downside of indexing with square brackets is that operations on multiple columns are not parallelised.

Outside of the use cases noted above Polars [strongly favours the expression API with `select` and `filter`](selecting_data_expressions.md) in favor of accessing by square bracket indexing.

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

| pandas                                                                | polars                           |
|-----------------------------------------------------------------------|----------------------------------|
| select row<br> `df.iloc[2]`                                           | `df[2, :]`                       |
| select several rows by their indices<br> `df.iloc[[2, 5, 6]]`         | `df[[2, 5, 6], :]`               |
| select slice of rows<br> `df.iloc[2:6]`                               | `df[2:6, :]`                     |
| select rows using a boolean mask<br> `df.iloc[True, True, False]`     | `df.filter([True, True, False])` |
| select rows by a predicate condition<br> `df.loc[df["A"] > 3]`        | `df[df["A"] > 3]`                |
| select slice of columns<br> `df.iloc[:, 1:3]`                         | `df[:, 1:3]`                     |
| select slice of columns by string order<br> `df.loc[:, "A":"Z"]`      | `df[:, "A":"Z"]`                 |
| select a single value (scalar)<br> `df.loc[2, "A"]`                   | `df[2, "A"]`                     |
| select a single value (scalar)<br> `df.iloc[2, 1]`                    | `df[2, 1]`                       |
| select a single value (Series/DataFrame)<br> `df.loc[2, ["A"]]`       | `df[2, ["A"]]`                   |
| select a single value (Series/DataFrame)<br> `df.iloc[2, [1]]`        | `df[2, [1]]`                     |
