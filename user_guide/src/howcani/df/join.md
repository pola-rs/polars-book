# Joins

Polars supports sorting behavior similar to other DataFrame libraries.

- Join on a single or multiple column(s)
- Left join
- Inner join
- Outer join

## Dataset

```python
{{#include ../../examples/join/dataset.py}}
print(df_a)
```

```text
{{#include ../../outputs/join/dataset_a.txt}}
```

```python
print(df_b)
```

```text
{{#include ../../outputs/join/dataset_b.txt}}
```

## Eager

```python
{{#include ../../examples/join/eager.py:2:}}
print(out)
```

```text
{{#include ../../outputs/join/eager.txt}}
```

## Lazy

```python
{{#include ../../examples/join/lazy.py:2:}}
print(out)
```

```text
{{#include ../../outputs/join/lazy.txt}}
```
