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

### Inner join

An `inner` join produces a `DataFrame` that contains only the rows where the join key exists in both `DataFrames`. Let's take for example the following two `DataFrames`:

```python
{{#include ../../examples/combining_data/inner_join_example.py:3:8}}
print(df_customers)
```

```text
{{#include ../../outputs/combining_data/df_customers.txt}}
```

```python
{{#include ../../examples/combining_data/inner_join_example.py:9:15}}
print(df_orders)
```

```text
{{#include ../../outputs/combining_data/df_orders.txt}}
```

To get a `DataFrame` with the orders and their associated customer we can do an `inner` join on the `customer_id` column:

```python
{{#include ../../examples/combining_data/inner_join_example.py:16:16}}
print(df_inner_join)
```

```text
{{#include ../../outputs/combining_data/df_inner_customer_join.txt}}
```

### Left join

The `left` join produces a `DataFrame` that contains all the rows from the left `DataFrame` and only the rows from the right `DataFrame` where the join key exists in the left `DataFrame`. If we now take the example from above and want to have a `DataFrame` with all the customers and their associated orders (regardless of whether they have placed an order or not) we can do a `left` join:

```python
{{#include ../../examples/combining_data/left_join_example.py:16:16}}
print(df_left_join)
```

```text
{{#include ../../outputs/combining_data/df_left_join.txt}}
```

Notice, that the fields for the customer with the `customer_id` of `3` are null, as there are no orders for this customer.

### Outer join

The `outer` join produces a `DataFrame` that contains all the rows from both `DataFrames`. Columns are null, if the join key does not exist in the `DataFrame`. Doing an `outer` join on the two `DataFrames` from above produces a similar `DataFrame` to the `left` join:

```python
{{#include ../../examples/combining_data/outer_join_example.py:16:16}}
print(df_outer_join)
```

```text
{{#include ../../outputs/combining_data/df_outer_join.txt}}
```

### Cross join

A `cross` join is a cartesian product of the two `DataFrames`. This means that every row in the left `DataFrame` is joined with every row in the right `DataFrame`. The `cross` join is useful for creating a `DataFrame` with all possible combinations of the columns in two `DataFrames`. Let's take for example the following two `DataFrames`:

```python
{{#include ../../examples/combining_data/cross_join_example.py:3:7}}
print(df_colors)
```

```text
{{#include ../../outputs/combining_data/df_colors.txt}}
```

```python
{{#include ../../examples/combining_data/cross_join_example.py:8:12}}
print(df_sizes)
```

```text
{{#include ../../outputs/combining_data/df_sizes.txt}}
```

We can create a `DataFrame` with all possible combinations of the colors and sizes with a `cross` join:

```python
{{#include ../../examples/combining_data/cross_join_example.py:13:13}}
print(df_cross_join)
```

```text
{{#include ../../outputs/combining_data/df_cross_join.txt}}
```

<br>

The `inner`, `left`, `outer` and `cross` join strategies are standard amongst dataframe libraries. We provide more details on the less familiar `semi`, `anti` and `asof` join strategies below.

### Semi join

Consider the following scenario: a car rental company has a `DataFrame` showing the cars that it owns with each car having a unique `id`.

```python
{{#include ../../examples/combining_data/semi_join_example.py:4:9}}
print(df_cars)
```

```text
{{#include ../../outputs/combining_data/df_cars.txt}}
```

The company has another `DataFrame` showing each repair job carried out on a vehicle.

```python
{{#include ../../examples/combining_data/semi_join_example.py:10:15}}
print(df_repairs)
```

```text
{{#include ../../outputs/combining_data/df_repairs.txt}}
```

You want to answer this question: which of the cars have had repairs carried out?

An inner join does not answer this question directly as it produces a `DataFrame` with multiple rows for each car that has had multiple repair jobs:

```python
{{#include ../../examples/combining_data/semi_join_example.py:16:16}}
print(df_inner_join)
```

```text
{{#include ../../outputs/combining_data/df_inner_join.txt}}
```

However, a semi join produces a single row for each car that has had a repair job carried out.

```python
{{#include ../../examples/combining_data/semi_join_example.py:17:17}}
print(df_semi_join)
```

```text
{{#include ../../outputs/combining_data/df_semi_join.txt}}
```

### Anti join

Continuing this example, an alternative question might be: which of the cars have **not** had a repair job carried out? An anti join produces a `DataFrame` showing all the cars from `df_cars` where the `id` is not present in the `df_repairs` `DataFrame`.

```python
{{#include ../../examples/combining_data/semi_join_example.py:18:18}}
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
{{#include ../../examples/combining_data/asof_join_example.py:5:16}}
print(df_trades)
```

```text
{{#include ../../outputs/combining_data/df_trades.txt}}
```

The broker has another `DataFrame` called `df_quotes` showing prices it has quoted for these stocks.

```python
{{#include ../../examples/combining_data/asof_join_example.py:18:29}}
print(df_quotes)
```

```text
{{#include ../../outputs/combining_data/df_quotes.txt}}
```

You want to produce a `DataFrame` showing for each trade the most recent quote provided *before* the trade. You do this with `join_asof` (using the default `strategy = "backward"`).
To avoid joining between trades on one stock with a quote on another you must specify an exact preliminary join on the stock column with `by="stock"`.

```python
{{#include ../../examples/combining_data/asof_join_example.py:30:30}}
print(df_asof_join)
```

```text
{{#include ../../outputs/combining_data/df_asof_join.txt}}
```

If you want to make sure that only quotes within a certain time range are joined to the trades you can specify the `tolerance` argument. In this case we want to make sure that the last preceding quote is within 1 minute of the trade so we set `tolerance = "1m"`.

```python
{{#include ../../examples/combining_data/semi_join_example.py:31:31}}
print(df_asof_tolerance_join)
```

```text
{{#include ../../outputs/combining_data/df_asof_tolerance_join.txt}}
```
