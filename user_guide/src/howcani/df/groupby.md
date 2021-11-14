# GroupBy

## Eager & Lazy

Groupby syntax is similar in both API's as both can use the expressions.
Grouping operations are done with the `.groupby()` method following by the `.agg()`
method.

In the `.agg()` method you can do as many aggregations on as many columns as you want.
Aggregation on all columns can be performed using the wildcard expression:
`.agg(pl.col("*").sum())`.

A quick (lazy) example:

```python
{{#include ../../examples/groupby/snippet.py}}
```

that would return:

```text
{{#include ../../outputs/groupby/output.txt}}
```
