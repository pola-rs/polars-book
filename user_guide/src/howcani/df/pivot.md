# Pivots

Pivot a column in a `DataFrame` and perform one of the following aggregations:

- first
- sum
- min
- max
- mean
- median

The pivot operation consists of a group by one, or multiple columns (these will be the new
y-axis), column that will be pivoted (this will be the new x-axis) and an aggregation.

## Dataset

```python
{{#include ../../examples/how_can_i/pivot/dataset.py}}
print(df)
```

```text
{{#include ../../outputs/how_can_i/pivot/dataset.txt}}
```

## Eager

```python
{{#include ../../examples/how_can_i/pivot/eager.py:4:}}
```

## Lazy

Lazy does not have a pivot in the API, to use pivots in `lazy`, we can use a `map` to apply an eager
custom function in a `lazy` computation node.

```python
{{#include ../../examples/how_can_i/pivot/lazy.py:4:}}
print(out)
```

```text
{{#include ../../outputs/how_can_i/pivot/lazy.txt}}
```
