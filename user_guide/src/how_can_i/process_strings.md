# How can I process strings

Polars exposes fast string processing methods. 

These operations are very fast as opposed to string operations in numpy / Pandas. 
In the latter, strings are stored as Python objects and during traversal the array/ Series the cpu needs to follow all 
the string pointers to different memory locations which expensive.

In Polars/ Arrow the strings are contiguous in memory and traversal is cache optimal and predictable for the cpu.

The string processing functions available are:
* [str_parse_date](POLARS_API_LINK/lazy/index.html#polars.lazy.Expr.str_parse_date)
* [str_contains](POLARS_API_LINK/lazy/index.html#polars.lazy.Expr.str_contains)
* [str_lengths](POLARS_API_LINK/lazy/index.html#polars.lazy.Expr.str_lengths)
* [str_replace](POLARS_API_LINK/lazy/index.html#polars.lazy.Expr.str_replace)
* [str_replace_all](POLARS_API_LINK/lazy/index.html#polars.lazy.Expr.str_replace_all)
* [str_to_lowercase](POLARS_API_LINK/lazy/index.html#polars.lazy.Expr.str_to_lowercase)
* [str_to_uppercase](POLARS_API_LINK/lazy/index.html#polars.lazy.Expr.str_to_uppercase)

## Examples

### string lengths

```python
{{#include ../examples/how_can_i/process_strings.py:1:7}}
print(str_lengths.collect())
```

```text
{{#include ../outputs/how_can_i_process_strings.txt}}
```

### contains

Below we use a regex pattern to filter articles (the, a, and, etc.) from a sentence.

```python
{{#include ../examples/how_can_i/process_strings.py:10:12}}
print(filtered.collect())
```

```text
{{#include ../outputs/how_can_i_process_strings_1.txt}}
```
