# Window functions 🚀🚀

Window functions are expressions with superpowers. They allow you to perform aggregations on groups in the
`select` context. Let's get a feel of what that means. First we create a dataset. The dataset loaded in the
snippet below contains information about pokemon and has the following columns:

`['#',  'Name',  'Type 1',  'Type 2',  'Total',  'HP',  'Attack',  'Defense',  'Sp. Atk',  'Sp. Def',  'Speed',  'Generation',  'Legendary']`

```python
{{#include ../examples/expressions/window_1.py:0:}}
```

```text
{{#include ../outputs/expressions/window_1.txt}}
```

## Groupby Aggregations in selection

Below we show how to use window functions to group over different columns and perform an aggregation on them.
Doing so allows us to use multiple groupby operations in parallel, using a single query. The results of the aggregation
are projected back to the original rows. Therefore, a window function will always lead to a `DataFrame` with the same size
as the original.

Note how we call `.over("Type 1")` and `.over(["Type 1", "Type 2"])`. Using window functions we can aggregate
over different groups in a single `select` call!

The best part is, this won't cost you anything. The computed groups are cached and shared between different `window` expressions.

```python
{{#include ../examples/expressions/window_2.py:3:}}
```

```text
{{#include ../outputs/expressions/window_2.txt}}
```

## Operations per group

Window functions can do more than aggregation. They can also be viewed as an operation within a group. If, for instance, you
want to `sort` the values within a `group`, you can write `col("value").sort().over("group")` and voilà! We sorted by group!

Let's filter out some rows to make this more clear.

```python
{{#include ../examples/expressions/window_group_1.py:4:}}
print(filtered)
```

```text
{{#include ../outputs/expressions/window_group_1.txt}}
```

Observe that the group `Water` of column `Type 1` is not contiguous. There are two rows of `Grass` in between. Also note
that each pokemon within a group are sorted by `Speed` in `ascending` order. Unfortunately, for this example we want them sorted in
`descending` speed order. Luckily with window functions this is easy to accomplish.

```python
{{#include ../examples/expressions/window_group_2.py:4:}}
print(out)
```

```text

{{#include ../outputs/expressions/window_group_2.txt}}
```

`Polars` keeps track of each group's location and maps the expressions to the proper row locations. This will also work
over different groups in a single `select`.

The power of window expressions is that you often don't need a `groupby -> explode` combination, but you can put the logic in a
single expression. It also makes the API cleaner. If properly used a:

- `groupby` -> marks that groups are aggregated and we expect a `DataFrame` of size `n_groups`
- `over` -> marks that we want to compute something within a group, but doesn't modify the original size of the `DataFrame`

## Window expression rules

The evaluations of window expressions are as follows (assuming we apply it to a `pl.Int32` column):

```python
# aggregate and broadcast within a group
# output type: -> Int32
pl.sum("foo").over("groups")

# sum within a group and multiply with group elements
# output type: -> Int32
(pl.col("x").sum() * pl.col("y")).over("groups")

# sum within a group and multiply with group elements 
# and aggregate the group to a list
# output type: -> List(Int32)
(pl.col("x").sum() * pl.col("y")).list().over("groups")

# note that it will require an explicit `list()` call
# sum within a group and multiply with group elements 
# and aggregate the group to a list
# the flatten call explodes that list

# This is the fastest method to do things over groups when the groups are sorted
(pl.col("x").sum() * pl.col("y")).list().over("groups").flatten()
```

## More examples

For more exercise, below are some window functions for us to compute:

- sort all pokemon by type
- select the first `3` pokemon per type as `"Type 1"`
- sort the pokemon within a type by speed and select the first `3` as `"fastest/group"`
- sort the pokemon within a type by attack and select the first `3` as `"strongest/group"`
- sort the pokemon by name within a type and select the first `3` as `"sorted_by_alphabet"`

```python
{{#include ../examples/expressions/window_3.py:3:}}
```

```text
{{#include ../outputs/expressions/window_3.txt}}
```

## Flattened window function

If we have a window function that aggregates to a `list` like the example above with the following expression:

`pl.col("Name").sort_by(pl.col("Speed")).head(3).list().over("Type 1")`

This still works, but that
would give us a column type `List` which might not be what we want (this would significantly increase our memory usage!).

Instead we could `flatten`. This just turns our 2D list into a 1D array and projects that array/column back to our `DataFrame`.
This is very fast because the reshape is often free, and adding the column back the the original `DataFrame` is also a lot cheaper (since we don't require a join like in a normal window function).

However, for this operation to make sense, it is important that the columns used in `over([..])` are sorted!
