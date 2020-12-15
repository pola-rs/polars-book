# Numpy interoperability

Polars Series have support for numpy's [universal functions](https://numpy.org/doc/stable/reference/ufuncs.html).
That means that numpys elementwise function like `np.exp`, `np.cos`, `np.div`, etc. all work with almost zero overhead.
There are few gotcha's however. 

* Missing values are a separate bitmask and are not visible by numpy
    - ✗ a window function or a convolve can therefore give flawed results.
    - ✔ elementwise functions preserve missing values

## Conversion
You can convert a `Series` to a numpy array with the `.to_numpy` method. Missing values will be replaced by `NaN` during
the conversion. If the Series doesn't have missing values, or you don't care about them, you can use the `.view` method.
This provides a zero copy numpy array of the `Series` data.
