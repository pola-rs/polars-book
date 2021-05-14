# Sorting

Polars supports sorting behavior similar to other DataFrame libraries, that is sorting
by one or multiple columns and in multiple/different orders.

## Dataset

```python
{{#include ../../examples/sorting/dataset.py}}
print(df)
```

```text
{{#include ../../outputs/sorting/dataset.txt}}
```

## Eager

```python
{{#include ../../examples/sorting/eager.py:3:}}
print(out)
```

```text
{{#include ../../outputs/sorting/eager.txt}}
```

## Lazy

```python
{{#include ../../examples/sorting/lazy.py:2:}}
print(out)
```

```text
{{#include ../../outputs/sorting/lazy.txt}}
```
