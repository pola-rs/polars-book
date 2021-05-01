# Apply window functions

`Polars` supports window functions inspired by
[PostgreSQL](https://www.postgresql.org/docs/current/tutorial-window.html). `Pandas`
users may recognize these as a `groupby.transform(aggregation)`.

`Polars` window functions are much more elegant than `Pandas` transform. We can apply
multiple functions over multiple columns in a single expression!

```python
{{#include ../../_examples/window-functions/snippet.py}}
```

```text
{{#include ../../_outputs/window-functions/output.txt}}
```
