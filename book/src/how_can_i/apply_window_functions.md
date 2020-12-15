# How can I apply window functions?

Polars supports window functions inspired by [postgres](https://www.postgresql.org/docs/9.1/tutorial-window.html). Pandas
users may know these as a `groupby.transform(aggregation)`. 

Polars window functions are much more elegant than Pandas transform. We can apply multiple functions over multiple columns in 
single expression!


## Examples
```python
{{#include ../examples/how_can_i/apply_window_functions.py:1:11}}

print(df)
```

```text
{{#include ../outputs/how_can_i_apply_window_functions_0.txt}}
```

```python
{{#include ../examples/how_can_i/apply_window_functions.py:12:18}}

print(windows.collect())
```

```text
{{#include ../outputs/how_can_i_apply_window_functions_1.txt}}
