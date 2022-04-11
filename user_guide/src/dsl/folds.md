# Folds

`Polars` provides expressions/methods for horizontal aggregations like [`sum`](POLARS_PY_REF_GUIDE/api/polars.DataFrame.sum.html),
[`min`](POLARS_PY_REF_GUIDE/api/polars.DataFrame.min.html), [`mean`](POLARS_PY_REF_GUIDE/api/polars.DataFrame.mean.html),
etc. by setting the argument `axis=1`. However, when you need a more complex aggregation the default methods provided by the
`Polars` library may not be sufficient. That's when `folds` come in handy.

The `Polars` `fold` expression operates on columns for maximum speed. It utilizes the data layout very efficiently and often has vectorized execution.

Let's start with an example by implementing the `sum` operation ourselves, with a `fold`.

## Manual Sum

```python
{{#include ../examples/expressions/fold_1.py:4:}}
print(out)
```

```text
{{#include ../outputs/expressions/folds_1.txt}}
```

The snippet above recursively applies the function `f(acc, x) -> acc` to an accumulator `acc` and a new column `x`.
The function operates on columns individually and can take advantage of cache efficiency and vectorization.

## Conditional

In the case where you'd want to apply a condition/predicate on all columns in a `DataFrame` a `fold` operation can be
a very concise way to express this.

```python
{{#include ../examples/expressions/fold_2.py:4:}}
print(out)
```

```text
{{#include ../outputs/expressions/folds_2.txt}}
```

In the snippet we filter all rows where **each** column value is `>` `1`.

## Folds and string data

Folds could be used to concatenate string data. However, due to the materialization of intermediate columns, this
operation will have squared complexity.

Therefore, we recommend using the `concat_str` expression for this.

```python
{{#include ../examples/expressions/fold_3.py:3:}}
print(out)
```

```text
{{#include ../outputs/expressions/folds_3.txt}}
```
