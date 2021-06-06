# Process strings

Thanks to its `Arrow` backend `Polars` string operations are much faster compared to the
same operations performed with `NumPy` or `Pandas`. In the latter, strings are stored as
`Python` objects and while traversing the `np.array` or the `pd.Series` the CPU needs to
follow all the string pointers, and jump to many random memory locations; which
is very cache inefficient. In `Polars` (*e.g.*, `Arrow` data
structure) strings are contiguous in memory and traversing is cache-optimal and
predictable for the CPU.

The string processing functions available in `Polars` are available in the
[`str` namespace](POLARS_PY_REF_GUIDE_V2/polars/series/StringNameSpace.html)

A few examples below. To compute string lengths:

```python
{{#include ../../examples/strings/snippet1.py}}
```

returning:

```text
{{#include ../../outputs/strings/output1.txt}}
```

And below a regex pattern to filter out articles (`the`, `a`, `and`, *etc.*) from a
sentence:

```python
{{#include ../../examples/strings/snippet2.py}}
```

yielding:

```text
{{#include ../../outputs/strings/output2.txt}}
```
