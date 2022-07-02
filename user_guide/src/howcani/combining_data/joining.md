# Joins

## Join strategies

`Polars` supports the following join strategies by specifying the `strategy` argument:

- `inner`
- `left`
- `outer`
- `cross`
- `asof`
- `semi`
- `anti`

The `inner`, `left`, `outer` and `cross` join strategies are standard amongst dataframe libraries. We provide more details on the less familiar `semi`, `anti` and `asof` join strategies below.

### Semi join

Consider the following scenario: a car rental company has a `DataFrame` showing the cars that it owns with each car having a unique `id`.

```python
{{#include ../../examples/combining_data/combining_data_examples.py:66:71}}
print(df_cars)
```

```text
{{#include ../../outputs/combining_data/df_cars.txt}}
```

The company has another `DataFrame` showing each repair job carried out on a vehicle.

```python
{{#include ../../examples/combining_data/combining_data_examples.py:72:77}}
print(df_repairs)
```

```text
{{#include ../../outputs/combining_data/df_repairs.txt}}
```

You want to answer this question: which of the cars have had repairs carried out?

An inner join does not answer this question directly as it produces a `DataFrame` with multiple rows for each car that has had multiple repair jobs:

```python
{{#include ../../examples/combining_data/combining_data_examples.py:78:78}}
print(df_inner_join)
```

```text
{{#include ../../outputs/combining_data/df_inner_join.txt}}
```

However, a semi join produces a single row for each car that has had a repair job carried out.

```python
{{#include ../../examples/combining_data/combining_data_examples.py:79:79}}
print(df_semi_join)
```

```text
{{#include ../../outputs/combining_data/df_semi_join.txt}}
```

### Anti join

Continuing this example, an alternative question might be: which of the cars have **not** had a repair job carried out? An anti join produces a `DataFrame` showing all the cars from `df_cars` where the `id` is not present in the `df_repairs` `DataFrame`.

```python
{{#include ../../examples/combining_data/combining_data_examples.py:80:80}}
print(df_anti_join)
```

```text
{{#include ../../outputs/combining_data/df_anti_join.txt}}
```

### Asof join

An `asof` join is like a left join except that we match on nearest key rather than equal keys.
In `Polars` we can do an asof join with the `join` method and specifying `strategy="asof"`. However, for more flexibility we can use the `join_asof` method.

Consider the following scenario: a stock market broker has a `DataFrame` called `df_trades` showing transactions it has made for different stocks.

```python
{{#include ../../examples/combining_data/combining_data_examples.py:82:95}}
print(df_trades)
```

```text
{{#include ../../outputs/combining_data/df_trades.txt}}
```

The broker has another `DataFrame` called `df_quotes` showing prices it has quoted for these stocks.

```python
{{#include ../../examples/combining_data/combining_data_examples.py:97:108}}
print(df_quotes)
```

```text
{{#include ../../outputs/combining_data/df_quotes.txt}}
```

You want to produce a `DataFrame` showing for each trade the most recent quote provided *before* the trade. You do this with `join_asof` (using the default `strategy = "backward"`).
To avoid joining between trades on one stock with a quote on another you must specify an exact preliminary join on the stock column with `by="stock"`.

```python
{{#include ../../examples/combining_data/combining_data_examples.py:109:109}}
print(df_asof_join)
```

```text
{{#include ../../outputs/combining_data/df_asof_join.txt}}
```

If you want to make sure that only quotes within a certain time range are joined to the trades you can specify the `tolerance` argument. In this case we want to make sure that the last preceding quote is within 1 minute of the trade so we set `tolerance = "1m"`.

```python
{{#include ../../examples/combining_data/combining_data_examples.py:112:112}}
print(df_asof_tolerance_join)
```

```text
{{#include ../../outputs/combining_data/df_asof_tolerance_join.txt}}
```
