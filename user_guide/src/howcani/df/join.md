# Joins

Polars supports sorting behavior similar to other DataFrame libraries.

- Join on a single or multiple column(s)
- Left join
- Inner join
- Outer join

## Dataset

```python
{{#include ../../examples/how_can_i/joins/dataset.py}}
print(df_a)
```

```text
{{#include ../../outputs/how_can_i/joins/dataset_a.txt}}
```

```python
print(df_b)
```

```text
{{#include ../../outputs/how_can_i/joins/dataset_b.txt}}
```

## Eager

```python
{{#include ../../examples/how_can_i/joins/eager.py:4:}}
print(out)
```

```text
{{#include ../../outputs/how_can_i/joins/eager.txt}}
```

## Lazy

```python
{{#include ../../examples/how_can_i/joins/lazy.py:5:}}
print(out)
```

```text
{{#include ../../outputs/how_can_i/joins/lazy.txt}}
```
