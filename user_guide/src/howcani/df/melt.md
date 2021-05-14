# Melts

Melt operations unpivot a DataFrame from wide format to long format

## Dataset

```python
{{#include ../../examples/melt/dataset.py}}
print(df)
```

```text
{{#include ../../outputs/melt/dataset.txt}}
```

## Eager + Lazy

`Eager` and `lazy` have the same API.

```python
{{#include ../../examples/melt/eager.py:3:}}
print(out)
```

```text
{{#include ../../outputs/melt/eager.txt}}
```
