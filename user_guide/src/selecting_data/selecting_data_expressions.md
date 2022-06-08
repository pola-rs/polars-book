# Selecting with expressions

In this page we cover

- use of the Expression API via the `filter` and `select` methods to select data
- combining these expressions and
- optimization of these expression in lazy mode.

To select data with expressions we use:

- the `filter` method to select rows
- the `select` method to select columns

For simplicity we deal with `DataFrame` examples throughout. The principles are the same for `Series` objects except that columns obviously cannot be selected in a `Series`. To illustrate the `filter` and `select` methods we define a simple `DataFrame`:

```python
{{#include ../examples/selecting_data/indexing_selecting_examples.py:4:10}}
print(df)
```

```text
{{#include ../outputs/selecting_data/simple_df.txt}}
```

## Selecting rows with the `filter` method

We can select rows by using the `filter` method. In the `filter` method we pass the condition we are using to select the rows as an expression:

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

# Selecting rows and columns

We can combine the `filter` and `select` methods to select rows and columns

```python
{{#include ../examples/selecting_data/indexing_selecting_examples.py:14:14}}
print(expression_df)
```

```text
{{#include ../outputs/selecting_data/expression_df.txt}}
```

# Query optimization

In lazy mode the query optimizer may be able to optimize the query based on the expressions.

In this example we scan a CSV file with many columns using `scan_csv` and then `select` a subset of them. The query optimizer creates a query plan that causes only the selected columns to be read from the CSV - see how the `Project` part of the query plan below states that only 2 of 13 columns will be read:

```python
{{#include ../examples/selecting_data/lazy_select_data.py:3:3}}
print(lazy_select_df.describe_optimized_plan())
```

```text
{{#include ../outputs/selecting_data/lazy_select_df.txt}}
```

If you specify two separate filter conditions the query optimizer will combine them into a single joint condition (see the `Selection` part of the query plan below):

```python
{{#include ../examples/selecting_data/lazy_select_data.py:8:8}}
print(lazy_filter_df.describe_optimized_plan())
```

```text
{{#include ../outputs/selecting_data/lazy_filter_df.txt}}
```
