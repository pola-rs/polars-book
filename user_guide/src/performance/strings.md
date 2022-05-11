# Strings

Understanding the memory format used by `Arrow` and `Polars` can really increase performance
of your queries. This is especially true for large string data. The figure below shows
how an `Arrow` `UTF8` array is laid out in memory.

The array `["foo", "bar", "ham"]` is encoded by :

- a concatenated string `"foobarham"`,
- an offset array indicating the start (and end) of each string `[0, 2, 5, 8]`,
- a null bitmap, indicating null values.

![](https://raw.githubusercontent.com/pola-rs/polars-static/master/docs/arrow-string.svg)

This memory structure is very cache-efficient if we are to read the string values.
Especially if we compare it to a `Vec<String>` (an array of heap allocated string data
in `Rust`).

![](https://raw.githubusercontent.com/pola-rs/polars-static/master/docs/pandas-string.svg)

However, if we need to reorder the `Arrow` `UTF8` array, we need to swap around all the
bytes of the string values, which can become very expensive when dealing with large
strings. On the other hand for `Vec<String>`, we only need to swap pointers around,
which is only 8 bytes data that have to be moved with little cost.

Reordering a `DataFrame` embedding a large number of `Utf8` `Series` due to an operation
(filtering, joining, grouping, *etc.*) can quickly become quite expensive.

## Categorical type

For this reason `Polars` has a `CategoricalType`. A `Categorical` `Series` is an array
filled with `u32` values that each represent a unique string value. Thereby maintaining
cache efficiency whilst remaining cheap to move values around.

In the example below we demonstrate how you can cast a `Utf8` `Series` column to a
`Categorical` `Series`.

```python
import polars as pl

df["utf8-column"].cast(pl.Categorical)
```

### Eager join multiple DataFrames on Categorical data

When two `DataFrames` need to be joined based on string data the `Categorical` data needs
to be synchronized (data in column `A` of `df1` needs to point to the same underlying
string data as column `B` in `df2`). One can do so by casting data in the `StringCache`
context manager. This will synchronize all discoverable string values for the duration of that
context manager. If you want the global string cache to exist during the whole
run, you can set `toggle_string_cache` to `True`.

```python
{{#include ../examples/strings_performance/snippet1.py}}
```

### Lazy join multiple DataFrames on Categorical data

A lazy query always has a global string cache (unless you opt-out) for the duration of
that query (until `.collect()` is called). The example below shows how you could join
two `DataFrames` with `Categorical` types.

```python
{{#include ../examples/strings_performance/snippet2.py}}
```
