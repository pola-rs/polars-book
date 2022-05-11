# Apply custom functions

There will always be an operation that is so particular that one cannot do it with the public API of
`Polars`. Luckily polars allows you to apply custom functions. This means one can
define a `Python` function (or `lambda`) and pass it to the logical plan.

Let's say we want to apply a mapping operation to a `Polars` `Series` in a eager
fashion. This could be done as shown below:

```python
{{#include ../../examples/udfs/snippet1.py}}
```

returning:

```text
{{#include ../../outputs/udfs/output1.txt}}
```

There are a few gotchas however, due to the fact `Polars` `Series` can only contain a
single datatype.

In the `.apply()` method above we did not specify the datatype the `Series` should
contain. `Polars` tries to infer the output datatype beforehand by calling the provided
function itself. If it later gets a datatype that does not match the initially inferred
type, the value will be indicated as missing (`null`).

If the output dtype is already known, it is thus recommended to provide that information to `Polars` (via
the `dtype` option of `.apply()`).

Note it is possible to change datatype as a result of applying a function: the `lambda`
we used above got an integer as input and returned a string (`pl.Utf8`) after finding
the right key in the `my_map` dictionary.

# to map or to apply?

There are two way to use custom function, either by using `map`, or by using `apply`. Which one you need depends on
the context where the custom functions are used:

- `apply`

  - selection context: the custom function is applied over all values `Fn(value) -> y`
  - groupby context: the custom function is applied over all groups `Fn([group_value_1, ... group_value_n]) -> y`

- `map`

  - selection context: the custom function is applied `Series` and must produce a new `Series` `Fn(Series) -> Series`
  - groupby context: the custom function is applied `Series` and must produce a new `Series` `Fn(Series) -> Series`
