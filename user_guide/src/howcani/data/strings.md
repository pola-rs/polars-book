# Process strings

Thanks to its `Arrow` backend `Polars` string operations are much faster compared to the same operations performed with `NumPy` or `Pandas`. 
In the latter, strings are stored as `Python` objects and while traversing the `np.array` or the `pd.Series` the CPU needs to follow all the string pointers, and jump through many different memory locations; which is, as expected, quite computationally expensive.
In `Polars` (*e.g.*, `Arrow` data structure) strings are contiguous in memory and traversing is cache-optimal and predictable for the CPU.

The string processing functions available in `Polars` are:

* [`.str_parse_date()`](POLARS_PY_REF_GUIDE/lazy/index.html#polars.lazy.Expr.str_parse_date)
* [`.str_contains()`](POLARS_PY_REF_GUIDE/lazy/index.html#polars.lazy.Expr.str_contains)
* [`.str_lengths()`](POLARS_PY_REF_GUIDE/lazy/index.html#polars.lazy.Expr.str_lengths)
* [`.str_replace()`](POLARS_PY_REF_GUIDE/lazy/index.html#polars.lazy.Expr.str_replace)
* [`.str_replace_all()`](POLARS_PY_REF_GUIDE/lazy/index.html#polars.lazy.Expr.str_replace_all)
* [`.str_to_lowercase()`](POLARS_PY_REF_GUIDE/lazy/index.html#polars.lazy.Expr.str_to_lowercase)
* [`.str_to_uppercase()`](POLARS_PY_REF_GUIDE/lazy/index.html#polars.lazy.Expr.str_to_uppercase)

A few examples below. To compute string lengths:

```python
{{#include ../../_examples/strings/snippet1.py}}
```

returning:

```text
{{#include ../../_outputs/strings/output1.txt}}
```

And below a regex pattern to filter out articles (`the`, `a`, `and`, *etc.*) from a sentence:

```python
{{#include ../../_examples/strings/snippet2.py}}
```

yielding:

```text
{{#include ../../_outputs/strings/output2.txt}}
```
