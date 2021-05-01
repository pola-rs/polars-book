# Conditionally apply

One often want to modify or add a column to a DataFrame based on some condition/predicate.
This is where the `.when()`/`.then()`/`.otherwise()` expressions come into play.
As they are basically a full English sentence, they need no further explanation.

See:

```python
{{#include ../../_examples/conditionally-apply/snippet.py}}
```

yielding:

```text
{{#include ../../_outputs/conditionally-apply/output.txt}}
```
