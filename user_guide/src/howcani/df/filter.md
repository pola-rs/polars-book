# Filter

## Eager

Filter operation in Eager are very similar to what you are used in `Pandas`.

```python
{{#include ../../examples/filter/eager.py}}
```

or in more idiomatic `Polars` way:

```python
df.filter(pl.col("a") > 2)
```

## Lazy

Filters operations in Lazy are expressed as:

```python
{{#include ../../examples/filter/lazy.py:2:}}
```

Both result in:

```text
{{#include ../../outputs/filter/filter.txt}}
```
