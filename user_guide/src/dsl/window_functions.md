# Window functions 🚀🚀

Window functions are expressions with superpowers. They allow you to do aggregation on groups in the
**select** context. Let's get a feel of what that means. First we create a dataset. The dataset loaded in the
snippet below contains information about pokemon and has the following columns:

`['#',  'Name',  'Type 1',  'Type 2',  'Total',  'HP',  'Attack',  'Defense',  'Sp. Atk',  'Sp. Def',  'Speed',  'Generation',  'Legendary']`

```python
{{#include ../examples/expressions/window_1.py:0:}}
```

```text
{{#include ../outputs/expressions/window_1.txt}}
```

## Groupby Aggregations in selection

Below we show how we use window function to group over different columns and do an aggregation on them.
Doing so, allows us to do multiple groupby operations in parallel in a single query. The results of the aggregation
are projected back to the original rows. A window function will therefore always lead to a DataFrame with the same size
as the original.

```python
{{#include ../examples/expressions/window_2.py:3:}}
```

```text
{{#include ../outputs/expressions/window_2.txt}}
```

## Operations per group

In case we want to do something on a group level, we can also use window functions. Below we flex our muscles using them:

We:

- sort all pokemon by type
- select the first 3 pokemon per type as `"Type 1"`
- sort the pokemon within a type by speed and select the first 3 as `"fastest/group"`
- sort the pokemon within a type by attack and select the first 3 as `"strongest/group"`
- sort the pokemon by name within a type and select the first 3 as `"sorted_by_alphabet"`

```python
{{#include ../examples/expressions/window_3.py:3:}}
```

```text
{{#include ../outputs/expressions/window_3.txt}}
```

## Flattened window function

If we have a window function that aggregates to a `list` like we did above with the following expression:
`pl.col("Name").sort_by(pl.col("Speed")).head(3).over("Type 1")` we could just leave it like that, but that
would give us a column type `List` which is often not what we want (and it increases our memory usage a lot!).

Instead we could `flatten`. This just turns our 2D list into a 1D array and projects that array/column back to our DataFrame.
This is very fast, because the reshape is often free and adding the column back the the original DataFrame is also a lot cheaper,
because we don't require a join like in a normal window function.

For this operation to make sense however, it is important that the columns used in `over([..])` are sorted!
