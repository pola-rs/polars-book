# How can I split / apply / combine?

This example shows how you idiomatically would determine differences per group. Let's imagine we have a dataset with
some unique identifier **uid**, some dates per **uid** as **date** column, and a number of cumulative COVID cases per
**date**. 

Now we want to find the determine the difference (i.e. the increase of COVID cases per day per group.)

## Dataset setup
First we create the example dataset of this problem.

```python
{{#include ../examples/how_can_i/split_apply_combine.py:1:24}}
print(df)
```

```text
{{#include ../outputs/how_can_i_split_apply_combine_1.txt}}
```


## Query
```python
{{#include ../examples/how_can_i/split_apply_combine.py:25:58}}
print(df)
```

```text
{{#include ../outputs/how_can_i_split_apply_combine_2.txt}}
```
