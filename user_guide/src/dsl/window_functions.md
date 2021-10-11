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
{{#include ../examples/expressions/window_2.py:5:}}
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
{{#include ../examples/expressions/window_3.py:5:}}
```

```text
{{#include ../outputs/expressions/window_3.txt}}
```
