# Conditionally apply

One often wants to modify or add a column to a DataFrame based on some
condition/predicate. This is where the `.when()`/`.then()`/`.otherwise()` expressions
come into play. As they are basically a full English sentence, they need no further
explanation.

See:

```python
{{#include ../../examples/conditionally_apply/snippet.py}}
```

yielding:

```text
{{#include ../../outputs/conditionally_apply/output.txt}}
```
