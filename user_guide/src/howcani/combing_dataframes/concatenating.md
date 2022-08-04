# Concatenation

There are a number of ways to concatenate data from separate DataFrames:

- two dataframes with **the same columns** can be **vertically** concatenated to make a **longer** dataframe
- two dataframes with the **same number of rows** and **non-overlapping columns** can be **horizontally** concatenated to make a **wider** dataframe
- two dataframes with **different numbers of rows and columns** can be **diagonally** concatenated to make a dataframe which might be longer and/ or wider. Where column names overlap values will be vertically concatenated. Where column names do not overlap new rows and columns will be added. Missing values will be set as `null`

## Vertical concatenation - getting longer

In a vertical concatenation you combine all of the rows from a list of `DataFrames` into a single longer `DataFrame`.

Vertical concatenation fails when the dataframes do not have the same columns.

## Horizontal concatenation - getting wider

In a horizontal concatenation you combine all of the columns from a list of `DataFrames` into a single wider `DataFrame`.

Horizontal concatenation fails when dataframes have overlapping columns.

## Diagonal concatenation - getting longer, wider and `null`ier

In a diagonal concatenation you combine all of the row and columns from a list of `DataFrames` into a single longer and/or wider `DataFrame`.

Diagonal concatenation generates nulls when the column names do not overlap.

## Rechunking

Before a concatenation we have two dataframes `df1` and `df2`. In memory each of these is a separate Arrow `Table`. By default these `Tables` are copied to a new combined table during the concatenatation - this is known as **rechunking**. Rechunking makes further operations on the concatenated `DataFrame` faster.

If you do not want Polars to rechunk the concatenated `DataFrame` and instead to keep track of which rows point to which original `Table` you specify `rechunk = False` when doing the concatenation.
