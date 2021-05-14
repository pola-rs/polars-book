# Common manipulations

Like other DataFrame libaries, Polars provides a wide range of common functions to
manipulate a Datframe. Users that are familiar with Dataframes will see many
similarities.

## Add columns

```python
{{#include ../../examples/df_manipulations/add_column.py}}
```

```text
{{#include ../../outputs/df_manipulations/add_column.txt}}
```

## Type casting

```python
{{#include ../../examples/df_manipulations/casting.py}}
```

```text
{{#include ../../outputs/df_manipulations/casting.txt}}
```

## Rename column

```python
{{#include ../../examples/df_manipulations/rename_column.py}}
```

```text
{{#include ../../outputs/df_manipulations/rename_column.txt}}
```

## Drop column

```python
{{#include ../../examples/df_manipulations/drop_column.py}}
```

```text
{{#include ../../outputs/df_manipulations/drop_column.txt}}
```

## Drop nulls

```python
df.drop_nulls()
```

```text
{{#include ../../outputs/df_manipulations/drop_nulls.txt}}
```

## Fill NA

Other strategies:

- `mean`
- `backward`
- `min`
- `max`

```python
df.fill_none('forward')
```

```text
{{#include ../../outputs/df_manipulations/fill_na.txt}}
```

## Get columns

```python
df.columns
```

```text
{{#include ../../outputs/df_manipulations/get_columns.txt}}
```

## Null Count

```python
df.null_count()
```

```text
{{#include ../../outputs/df_manipulations/null_count.txt}}
```

## Sort columns

```python
df.sort('a', reverse=True)
```

```text
{{#include ../../outputs/df_manipulations/sort_columns.txt}}
```

## To Numpy

```python
df.to_numpy()
```

```text
{{#include ../../outputs/df_manipulations/to_numpy.txt}}
```

## To Pandas

```python
df.to_pandas()
```

```text
{{#include ../../outputs/df_manipulations/to_pandas.txt}}
```
