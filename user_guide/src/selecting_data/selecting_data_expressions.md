# Selecting with expressions
In this page we cover use of the `filter` and `select` methods to select data, combining these expressions and optimization of these expression in lazy mode.

To select data with expressions we use:
- the `filter` method to select rows
- the `select` method to select columns

To illustrate both of these methods we define a simple `DataFrame`:
```python
{{#include ../examples/selecting_data/indexing_selecting_examples.py:4:10}}
print(df)
```

```text
{{#include ../outputs/selecting_data/simple_df.txt}}
```
## Selecting rows with the `filter` method
We can select rows by using the `filter` method. In the `filter` method we pass the condition we are using to select the rows:
```python
{{#include ../examples/selecting_data/indexing_selecting_examples.py:16:16}}
print(filter_df)
```

```text
{{#include ../outputs/selecting_data/filter_df.txt}}
```
We can specify multiple conditions in `filter` using the `&` operator:
```python
{{#include ../examples/selecting_data/indexing_selecting_examples.py:18:18}}
print(multi_filter_df)
```

```text
{{#include ../outputs/selecting_data/multi_filter_df.txt}}
```

## Selecting columns with the `select` method
We select columns using the `select` method. In the `select` method we can specify the columns with:
- a (string) column name
- a list of (string) column names
- a boolean list of the same length as the number of columns
- an expression such as a condition on the column name
- a `Series`

### Select a single column
```python
{{#include ../examples/selecting_data/indexing_selecting_examples.py:20:20}}
print(single_select_df)
```

```text
{{#include ../outputs/selecting_data/single_select_df.txt}}
```
### Select a list of columns
```python
{{#include ../examples/selecting_data/indexing_selecting_examples.py:22:22}}
print(list_select_df)
```

```text
{{#include ../outputs/selecting_data/list_select_df.txt}}
```
### Select based on a Boolean list:

```python
{{#include ../examples/selecting_data/indexing_selecting_examples.py:24:26}}
print(boolean_list_select_df)
```

```text
{{#include ../outputs/selecting_data/boolean_list_select_df.txt}}
```

### Select columns with an expression
To select based on a condition on the column name:
```python
{{#include ../examples/selecting_data/indexing_selecting_examples.py:28:28}}
print(condition_select_df)
```

```text
{{#include ../outputs/selecting_data/condition_select_df.txt}}
```

To select based on the dtype of the columns:
```python
{{#include ../examples/selecting_data/indexing_selecting_examples.py:30:30}}
print(dtype_select_df)
```

```text
{{#include ../outputs/selecting_data/dtype_select_df.txt}}
```
