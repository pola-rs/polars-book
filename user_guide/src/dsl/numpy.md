# Numpy interop

`Polars` expressions support `NumPy` [ufuncs](https://numpy.org/doc/stable/reference/ufuncs.html). See [here](https://numpy.org/doc/stable/reference/ufuncs.html#available-ufuncs)
for a list on all supported numpy functions.

This means that if a function is not provided by `Polars`, we can use `NumPy` and we still have fast columnar operation through
the `NumPy` API.

## Example

```python
{{#include ../examples/expressions/numpy_ufunc.py}}
print(out)
```

```text
{{#include ../outputs/expressions/np_ufunc_1.txt}}
```

## Gotcha's

Read more about the [gotcha's here](POLARS_ROOT/howcani/interop/numpy.html).
