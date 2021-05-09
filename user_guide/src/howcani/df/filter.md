# Filter

## Eager

Filter operation in Eager are very similar to what you are used in `Pandas`.

```python
{{#include ../../examples/how_can_i/filter/eager_1.py}}
```

or in more idiomatic `Polars` way:

```python
df.filter(col("a") > 2)
```

## Lazy

Filters operations in Lazy are expressed as:

```python
{{#include ../../examples/how_can_i/filter/lazy.py:5:}}
```

Both result in:

```text
{{#include ../../outputs/howcani/filter/filter.txt}}
```
