# Conditionally apply

Modifying a `Series` or a column in a `DataFrame` consists of two steps.

1. Creating a `boolean` `mask` based on some predicate.
1. Replace the values where the `mask` evaluates `True`
1. (Only in lazy) Define values where the mask evaluates `False`

## Dataset

```python
{{#include ../../examples/how_can_i/conditionally_apply/dataset.py}}
df.head()
```

```text
{{#include ../../outputs/how_can_i/conditionally_apply/dataset.txt}}
```

## Eager

```python
{{#include ../../examples/how_can_i/conditionally_apply/eager.py:6:}}
```

```text
{{#include ../../outputs/how_can_i/conditionally_apply/eager.txt}}
```

## Lazy

In lazy we can use the `.when()`/`.then()`/`.otherwise()` expressions.

- `when` - accepts a predicate expression
- `then` - expression to use when `predicate == True`
- `otherwise` - expression to use when `predicate == False`

See:

```python
{{#include ../../examples/how_can_i/conditionally_apply/lazy.py:4:}}
print(df)
```

```text
{{#include ../../outputs/how_can_i/conditionally_apply/lazy.txt}}
```
