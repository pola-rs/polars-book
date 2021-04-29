## Performance and string data
Understanding the memory format used by Arrow/ Polars can really increase performance of your
queries. This is especially true for large string data. The figure below shows how an Arrow UTF8
array is laid out in memory.

The array `["foo", "bar", "ham"]` is encoded by 

  * a concatenated string `"foobarham"`
  * an offset array indicating the start (and end) of each string `[0, 2, 5, 8]`
  * a null bitmap, indicating null values

![](https://raw.githubusercontent.com/ritchie46/img/master/polars/arrow/arrow_string.svg)

This memory structure is very cache efficient if we are to read the string values. Especially if
we compare it to a `Vec<String>` (an array of heap allocated string data in Rust).

![](https://raw.githubusercontent.com/ritchie46/img/master/polars/arrow/pandas_string.svg)

However, if we need to reorder the Arrow UTF8 array, we need to swap around all the bytes of the
string values, which can become very expensive when we're dealing with large strings. On the
other hand, for the `Vec<String>`, we only need to swap pointers around which is only 8 bytes data
that have to be moved.

If you have a `DataFrame` with a large number of
Utf8 `Series` and you need to reorder them due to an
operation like a FILTER, JOIN, GROUPBY, etc. than this can become quite expensive.

## Categorical type
For this reason Polars has a `CategoricalType`. A Categorical
`Series` is an array filled with `u32` values that each represent a unique string value.
Thereby maintaining cache-efficiency, whilst also making it cheap to move values around.

### Example: Single DataFrame

In the example below we show how you can cast an Utf8 `Series` column to a Categorical `Series`.

```python
import polars as pl

df["utf8-column"].cast(pl.Categorical)
```

### Example: Eager join multiple DataFrames on a Categorical
When the strings of one column need to be joined with the string data from another `DataFrame`.
The `Categorical` data needs to be synchronized (Categories in `df A` need to point to the same
underlying string data as Categories in `df B`). You can do by casting data int he `StringCache` context manager. 
This will synchronize all seen string values for the duration of that context manager. If you want the global string cache
to be existent during the whole program run, you can set `toggle_string_cache` to `True`

```python
{{#include ../examples/performance/string_data.py:1:10}}
```

### Example: Lazy join multiple DataFrames on a Categorical
A lazy Query always has a global string cache (unless you opt-out) for the duration of that query (until `collect` is called).
The example below shows how you could join two DataFrames with Categorical types.

```python
{{#include ../examples/performance/string_data.py:11:18}}
```
