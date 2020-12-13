# How can I groupby?

The groupby operations is done with the `.groupby` method following by the `.agg` method.
In the `.agg` method you can do as many aggregations on as many columns as you want.

If you want to do a specific aggregation on all columns you can use the wildcard expression: `.agg(col("*").sum())`

## Examples

```python
{{#include ../examples/how_can_i/groupby.py:1:8}}
reddit.collect()
```

```text
{{#include ../outputs/how_can_i_groupby.txt}}
```
