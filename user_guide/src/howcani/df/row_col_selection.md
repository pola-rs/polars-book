# Row and column selection

Selection of rows and columns is similar to other DataFrame libraries.

## Column selection

```python
# preferred
df.select(["a", "b"])
# also works
df(["a", "b"])
```

```text
{{#include ../../outputs/row_col_selection/col_selection.txt}}
```

## Row selection

```python
df[0:2]
```

```text
{{#include ../../outputs/row_col_selection/row_selection.txt}}
```
