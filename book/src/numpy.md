# Numpy interoperability

Polars Series have support for numpy's [universal functions](https://numpy.org/doc/stable/reference/ufuncs.html).
That means that numpys elementwise function like `np.exp`, `np.cos`, `np.div`, etc. all work with almost zero overhead.
There are few gotcha's however. Missing values are ignored during the function application. They are maintained, as they
are just a separate bitmask. However, any function that depends on previous/next elements, i.e. a sum, a convolve etc.
should not be used or used with caution.

## Conversion
You can convert a `Series` to a numpy array with the `.to_numpy` method. Missing values will be replaced by `NaN` during
the conversion. If the Series doesn't have missing values, or you don't care about them, you can use the `.view` method.
This provides a zero copy numpy array of the `Series` data.
