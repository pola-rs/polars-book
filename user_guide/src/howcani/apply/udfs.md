# Apply custom functions

There will always be an operation so sketchy that one cannot do with the public API of
`Polars`. Luckily this latter supports User Defined Functions (UDFs). This means one can
define a `Python` function (or `lambda`) and pass it to the logical plan. Custom
functions can be used in both the eager and the lazy API.

## Eager

Let's say we want to apply a mapping operation to a `Polars` `Series` in a eager
fashion. This could be done as shown below:

```python
{{#include ../../_examples/udfs/snippet1.py}}
```

returning:

```text
{{#include ../../_outputs/udfs/output1.txt}}
```

There are a few gotchas however, due to the fact `Polars` `Series` can only contain a
single datatype.

In the `.apply()` method above we did not specify the datatype the `Series` should
contain. `Polars` tries to infer the output datatype beforehand by calling the provided
function itself. If it later gets a datatype that does not matche the initially inferred
type, the value will be indicated as missing (`null`).

If already known, it is thus recommended to provide the output datatype to `Polars` (via
the `dtype` option of `.apply()`).

Note it is possible to change datatype as a result of applying a function: the `lambda`
we used above got an integer as input and returned a string (`pl.Utf8`) after finding
the right key in the `my_map` dictionary.

## Lazy

Using the lazy API you can apply custom functions via the `.map` and the `.apply`
methods.

#### .map()

The `.map()` method maps a `Series` to a `Series` or a `DataFrame` to a `DataFrame`.

#### .apply()

The `apply` method operates on the values of a `Series` as the function passed to
`.apply()` should operate on a *single* primitive (*e.g.*, `int`, `str`, `bool`).

When a custom function is used, the output datatype *must* be provided as the schema of
the query has to be known at all time for the optimizer to do its job.

See:

```python
{{#include ../../_examples/udfs/snippet2.py}}
```

yielding:

```text
{{#include ../../_outputs/udfs/output2.txt}}
```

Above is defined a custom function that was added to the lazy query and ran during
execution of the physical plan. This of course greatly increases flexibility of a query,
and when needed above is definitely the recommended implementation.

**This is however not without cost.**

Even though only vectorized code is used in this example (`NumPy` functions and `Polars`
comparisons), this query may still be slower than a `Polars`-native query. Once again,
this is due to the `Python` GIL. As mentioned before, `Polars` tries to parallelize the
query execution on the available cores on your machine. However `Python` limits the
number of threads to a unique instance. Many UDFs have thus to be run sequentially.

An implementation similar to the eager example (applying a `lambda` function on the
elements of a `Series`) could be:

```python
{{#include ../../_examples/udfs/snippet3.py}}
```

returning:

```text
{{#include ../../_outputs/udfs/output3.txt}}
```

#### GroupBy

One can also use custom functions in a grouping context. Below are shown three different
ways to get the length of each group, two using custom functions:

```python
{{#include ../../_examples/udfs/snippet4.py}}
```

And the respective outputs:

```text
{{#include ../../_outputs/udfs/output4.txt}}
```
