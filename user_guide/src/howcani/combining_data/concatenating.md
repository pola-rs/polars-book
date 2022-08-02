# Concatenation

There are a number of ways to concatenate data from separate DataFrames:

- two dataframes with **the same columns** can be **vertically** concatenated to make a **longer** dataframe
- two dataframes with the **same number of rows** and **non-overlapping columns** can be **horizontally** concatenated to make a **wider** dataframe
- two dataframes with **different numbers of rows and columns** can be **diagonally** concatenated to make a dataframe which might be longer and/ or wider. Where column names overlap values will be vertically concatenated. Where column names do not overlap new rows and columns will be added. Missing values will be set as `null`

## Vertical concatenation - getting longer

In a vertical concatenation you combine all of the rows from a list of `DataFrames` into a single longer `DataFrame`.

```python
{{#include ../../examples/combining_data/vertical_concat_example.py:4:22}}
print(df_vertical_concat)
```

```text
{{#include ../../outputs/combining_data/df_vertical_concat.txt}}
```

Vertical concatenation fails when the dataframes do not have the same column names.

## Horizontal concatenation - getting wider

In a horizontal concatenation you combine all of the columns from a list of `DataFrames` into a single wider `DataFrame`.

```python
{{#include ../../examples/combining_data/horizontal_concat_example.py:4:22}}
print(df_horizontal_concat)
```

```text
{{#include ../../outputs/combining_data/df_horizontal_concat.txt}}
```

Horizontal concatenation fails when dataframes have overlapping columns or a different number of rows.

## Diagonal concatenation - getting longer, wider and `null`ier

In a diagonal concatenation you combine all of the row and columns from a list of `DataFrames` into a single longer and/or wider `DataFrame`.

```python
{{#include ../../examples/combining_data/diagonal_concat_example.py:3:22}}
print(df_diagonal_concat)
```

```text
{{#include ../../outputs/combining_data/df_diagonal_concat.txt}}
```

Diagonal concatenation generates nulls when the column names do not overlap.

## Rechunking

Before a concatenation we have two dataframes `df1` and `df2`. Each column in `df1` and `df2` is in one or more chunks in memory. By default, during concatenation the chunks in each column are copied to a single new chunk - this is known as **rechunking**. Rechunking makes the join slower but further operations on the concatenated `DataFrame` faster.

If you do not want Polars to rechunk the concatenated `DataFrame` you specify `rechunk = False` when doing the concatenation. This approach makes the join faster but further operations on the concatenated `DataFrame` slower.
