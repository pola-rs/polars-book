# GroupBy

Grouping operations are done with the `.groupby()` method following by the `.agg()` method.

In the `.agg()` method you can do as many aggregations on as many columns as you want.
Aggregation on all columns can be performed using the wildcard expression: `.agg(col("*").sum())`.

A quick (lazy) example:

```python
{{#include ../../_examples/groupby/snippet.py}}
```

that would return:

```text
{{#include ../../_outputs/groupby/output.txt}}
```
