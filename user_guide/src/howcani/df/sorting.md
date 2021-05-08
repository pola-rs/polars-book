# Sorting

Polars supports sorting behavior similar to other DataFrame libraries, that is sorting
by one or multiple columns and in multiple/different orders.

## Dataset

```python
{{#include ../../examples/how_can_i/sorting/dataset.py}}
print(df)
```

```text
{{#include ../../outputs/how_can_i/sorting/dataset.txt}}
```

## Eager

```python
{{#include ../../examples/how_can_i/sorting/eager.py:4:}}
print(out)
```

```text
{{#include ../../outputs/how_can_i/sorting/eager.txt}}
```

## Lazy

```python
{{#include ../../examples/how_can_i/sorting/lazy.py:3:}}
print(out)
```

```text
{{#include ../../outputs/how_can_i/sorting/lazy.txt}}
```
