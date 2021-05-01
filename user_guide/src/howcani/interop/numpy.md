# NumPy

`Polars` `Series` have support for `NumPy` [universal functions (ufuncs)](https://numpy.org/doc/stable/reference/ufuncs.html).
Element-wise function such as `np.exp()`, `np.cos()`, `np.div()`, *etc.* all work with almost zero overhead.

A `Polars`-specific remark however: missing values are a separate bitmask and are not visible by `NumPy`.
It can yield to a window function or a `np.convolve()` giving flawed/incomplete results.

One can convert a `Polars` `Series` to a `NumPy` array with the `.to_numpy()` method.
Missing values will be replaced by `np.nan` during the conversion.
If the `Series` does not include missing values, or those values are not desired anymore, the `.view()` method can be used instead, providing a zero-copy `NumPy` array of the data.
