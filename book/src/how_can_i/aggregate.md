# How can I aggregate?

Aggregations can be done in a `.select` or a `.with_column`/`with_columns` method.

If you want to do a specific aggregation on all columns you can use the wildcard expression: `.select(col("*").sum())`

## Examples
```python
{{#include ../examples/how_can_i/aggregate.py:1:8}}
reddit.fetch()
```

```text
{{#include ../outputs/how_can_i_aggregate.txt}}
```
