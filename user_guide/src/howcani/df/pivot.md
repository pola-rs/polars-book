# Pivots

Pivot a column in a `DataFrame` and perform one of the following aggregations:

- first
- sum
- min
- max
- mean
- median

The pivot operation consists of a group by one, or multiple columns (these will be the
new y-axis), column that will be pivoted (this will be the new x-axis) and an
aggregation.

## Dataset

```python
{{#include ../../examples/pivot/dataset.py}}
print(df)
```

```text
{{#include ../../outputs/pivot/dataset.txt}}
```

## Eager

```python
{{#include ../../examples/pivot/eager.py:3:}}
```

## Lazy

A polars `LazyFrame` always need to no the schema of a computation statically (before collecting the query).
As a pivot's output schema depends on the data, and it is therefore impossible to determine the schema without
running the query.

Polars could have abstracted this fact for you just like Spark does, but we don't want you to shoot yourself in the foot
with a shotgun. The cost should be clear up front.

```python
{{#include ../../examples/pivot/lazy.py:3:}}
print(out)
```

```text
{{#include ../../outputs/pivot/lazy.txt}}
```
