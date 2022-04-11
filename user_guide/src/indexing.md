# Indexing

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

## Expressions

Expressions can also be used in indexing (it is syntactic sugar for `df.select`).

This can be used to do some pretty exotic selections.

```python
df[[
    pl.col("A").head(5),  # get first of "A"
    pl.col("B").tail(5).reverse(), # get last of "B" in reversed order
    pl.col("B").filter(pl.col("B") > 5).head(5), # get first of "B" that fulfils predicate
    pl.sum("A").over("B").head(5) # get the sum aggregation of "A" over the groups of "B" and return the first 5
]]
```
