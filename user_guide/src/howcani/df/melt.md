# Melts

Melt operations unpivot a DataFrame from wide format to long format

## Dataset

```python
{{#include ../../examples/how_can_i/melt/dataset.py}}
print(df)
```

```text
{{#include ../../outputs/how_can_i/melt/dataset.txt}}
```

## Eager + Lazy

`Eager` and `lazy` have the same API.

```python
{{#include ../../examples/how_can_i/melt/eager.py:4:}}
print(out)
```

```text
{{#include ../../outputs/how_can_i/melt/eager.txt}}
```
