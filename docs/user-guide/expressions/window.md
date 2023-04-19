# Window functions 

Window functions are expressions with superpowers. They allow you to perform aggregations on groups in the
`select` context. Let's get a feel of what that means. First we create a dataset. The dataset loaded in the
snippet below contains information about pokemon and has the following columns:

`['#',  'Name',  'Type 1',  'Type 2',  'Total',  'HP',  'Attack',  'Defense',  'Sp. Atk',  'Sp. Def',  'Speed',  'Generation',  'Legendary']`

=== ":fontawesome-brands-python: Python"
    ``` python
    --8<-- "user-guide/python/expressions/window.py:pokemon"
    ```

```
shape: (163, 13)
┌─────┬───────────────────────┬─────────┬────────┬───┬─────────┬───────┬────────────┬───────────┐
│ #   ┆ Name                  ┆ Type 1  ┆ Type 2 ┆ … ┆ Sp. Def ┆ Speed ┆ Generation ┆ Legendary │
│ --- ┆ ---                   ┆ ---     ┆ ---    ┆   ┆ ---     ┆ ---   ┆ ---        ┆ ---       │
│ i64 ┆ str                   ┆ str     ┆ str    ┆   ┆ i64     ┆ i64   ┆ i64        ┆ bool      │
╞═════╪═══════════════════════╪═════════╪════════╪═══╪═════════╪═══════╪════════════╪═══════════╡
│ 1   ┆ Bulbasaur             ┆ Grass   ┆ Poison ┆ … ┆ 65      ┆ 45    ┆ 1          ┆ false     │
│ 2   ┆ Ivysaur               ┆ Grass   ┆ Poison ┆ … ┆ 80      ┆ 60    ┆ 1          ┆ false     │
│ 3   ┆ Venusaur              ┆ Grass   ┆ Poison ┆ … ┆ 100     ┆ 80    ┆ 1          ┆ false     │
│ 3   ┆ VenusaurMega Venusaur ┆ Grass   ┆ Poison ┆ … ┆ 120     ┆ 80    ┆ 1          ┆ false     │
│ …   ┆ …                     ┆ …       ┆ …      ┆ … ┆ …       ┆ …     ┆ …          ┆ …         │
│ 147 ┆ Dratini               ┆ Dragon  ┆ null   ┆ … ┆ 50      ┆ 50    ┆ 1          ┆ false     │
│ 148 ┆ Dragonair             ┆ Dragon  ┆ null   ┆ … ┆ 70      ┆ 70    ┆ 1          ┆ false     │
│ 149 ┆ Dragonite             ┆ Dragon  ┆ Flying ┆ … ┆ 100     ┆ 80    ┆ 1          ┆ false     │
│ 150 ┆ Mewtwo                ┆ Psychic ┆ null   ┆ … ┆ 90      ┆ 130   ┆ 1          ┆ true      │
└─────┴───────────────────────┴─────────┴────────┴───┴─────────┴───────┴────────────┴───────────┘
```

## Groupby Aggregations in selection

Below we show how to use window functions to group over different columns and perform an aggregation on them.
Doing so allows us to use multiple groupby operations in parallel, using a single query. The results of the aggregation
are projected back to the original rows. Therefore, a window function will always lead to a `DataFrame` with the same size
as the original.

Note how we call `.over("Type 1")` and `.over(["Type 1", "Type 2"])`. Using window functions we can aggregate over different groups in a single `select` call!  Note that, in Rust, the type of the argument to `over()` must be a collection, so even when you're only using one column, you must provided it in an array.

The best part is, this won't cost you anything. The computed groups are cached and shared between different `window` expressions.


=== ":fontawesome-brands-python: Python"
    ``` python
    --8<-- "user-guide/python/expressions/window.py:groupby"
    ```

```
shape: (163, 5)
┌─────────┬────────┬────────────────────┬─────────────────────────────────┬────────────┐
│ Type 1  ┆ Type 2 ┆ avg_attack_by_type ┆ avg_defense_by_type_combination ┆ avg_attack │
│ ---     ┆ ---    ┆ ---                ┆ ---                             ┆ ---        │
│ str     ┆ str    ┆ f64                ┆ f64                             ┆ f64        │
╞═════════╪════════╪════════════════════╪═════════════════════════════════╪════════════╡
│ Grass   ┆ Poison ┆ 72.923077          ┆ 67.8                            ┆ 75.349693  │
│ Grass   ┆ Poison ┆ 72.923077          ┆ 67.8                            ┆ 75.349693  │
│ Grass   ┆ Poison ┆ 72.923077          ┆ 67.8                            ┆ 75.349693  │
│ Grass   ┆ Poison ┆ 72.923077          ┆ 67.8                            ┆ 75.349693  │
│ …       ┆ …      ┆ …                  ┆ …                               ┆ …          │
│ Dragon  ┆ null   ┆ 94.0               ┆ 55.0                            ┆ 75.349693  │
│ Dragon  ┆ null   ┆ 94.0               ┆ 55.0                            ┆ 75.349693  │
│ Dragon  ┆ Flying ┆ 94.0               ┆ 95.0                            ┆ 75.349693  │
│ Psychic ┆ null   ┆ 53.875             ┆ 51.428571                       ┆ 75.349693  │
└─────────┴────────┴────────────────────┴─────────────────────────────────┴────────────┘
```

## Operations per group

Window functions can do more than aggregation. They can also be viewed as an operation within a group. If, for instance, you
want to `sort` the values within a `group`, you can write `col("value").sort().over("group")` and voilà! We sorted by group!

Let's filter out some rows to make this more clear.

=== ":fontawesome-brands-python: Python"
    ``` python
    --8<-- "user-guide/python/expressions/window.py:operations"
    ```

```
shape: (7, 3)
┌─────────────────────┬────────┬───────┐
│ Name                ┆ Type 1 ┆ Speed │
│ ---                 ┆ ---    ┆ ---   │
│ str                 ┆ str    ┆ i64   │
╞═════════════════════╪════════╪═══════╡
│ Slowpoke            ┆ Water  ┆ 15    │
│ Slowbro             ┆ Water  ┆ 30    │
│ SlowbroMega Slowbro ┆ Water  ┆ 30    │
│ Exeggcute           ┆ Grass  ┆ 40    │
│ Exeggutor           ┆ Grass  ┆ 55    │
│ Starmie             ┆ Water  ┆ 115   │
│ Jynx                ┆ Ice    ┆ 95    │
└─────────────────────┴────────┴───────┘
```


Observe that the group `Water` of column `Type 1` is not contiguous. There are two rows of `Grass` in between. Also note
that each pokemon within a group are sorted by `Speed` in `ascending` order. Unfortunately, for this example we want them sorted in
`descending` speed order. Luckily with window functions this is easy to accomplish.

<div class="tabbed-blocks">

=== ":fontawesome-brands-python: Python"
    ``` python
    --8<-- "user-guide/python/expressions/window.py:sort"
    ```

```
shape: (7, 3)
┌─────────────────────┬────────┬───────┐
│ Name                ┆ Type 1 ┆ Speed │
│ ---                 ┆ ---    ┆ ---   │
│ str                 ┆ str    ┆ i64   │
╞═════════════════════╪════════╪═══════╡
│ Starmie             ┆ Water  ┆ 115   │
│ Slowpoke            ┆ Water  ┆ 30    │
│ SlowbroMega Slowbro ┆ Water  ┆ 30    │
│ Exeggutor           ┆ Grass  ┆ 55    │
│ Exeggcute           ┆ Grass  ┆ 40    │
│ Slowbro             ┆ Water  ┆ 15    │
│ Jynx                ┆ Ice    ┆ 95    │
└─────────────────────┴────────┴───────┘
```

`Polars` keeps track of each group's location and maps the expressions to the proper row locations. This will also work over different groups in a single `select`.

The power of window expressions is that you often don't need a `groupby -> explode` combination, but you can put the logic in a single expression. It also makes the API cleaner. If properly used a:

- `groupby` -> marks that groups are aggregated and we expect a `DataFrame` of size `n_groups`
- `over` -> marks that we want to compute something within a group, but doesn't modify the original size of the `DataFrame`

## Window expression rules

The evaluations of window expressions are as follows (assuming we apply it to a `pl.Int32` column):

=== ":fontawesome-brands-python: Python"
    ``` python
    --8<-- "user-guide/python/expressions/window.py:rules"
    ```

## More examples

For more exercise, below are some window functions for us to compute:

- sort all pokemon by type
- select the first `3` pokemon per type as `"Type 1"`
- sort the pokemon within a type by speed and select the first `3` as `"fastest/group"`
- sort the pokemon within a type by attack and select the first `3` as `"strongest/group"`
- sort the pokemon by name within a type and select the first `3` as `"sorted_by_alphabet"`

=== ":fontawesome-brands-python: Python"
    ``` python
    --8<-- "user-guide/python/expressions/window.py:examples"
    ```

```
shape: (43, 4)
┌────────┬─────────────────────┬─────────────────┬─────────────────────────┐
│ Type 1 ┆ fastest/group       ┆ strongest/group ┆ sorted_by_alphabet      │
│ ---    ┆ ---                 ┆ ---             ┆ ---                     │
│ str    ┆ str                 ┆ str             ┆ str                     │
╞════════╪═════════════════════╪═════════════════╪═════════════════════════╡
│ Bug    ┆ Paras               ┆ Metapod         ┆ Beedrill                │
│ Bug    ┆ Metapod             ┆ Kakuna          ┆ BeedrillMega Beedrill   │
│ Bug    ┆ Parasect            ┆ Caterpie        ┆ Butterfree              │
│ Dragon ┆ Dratini             ┆ Dratini         ┆ Dragonair               │
│ …      ┆ …                   ┆ …               ┆ …                       │
│ Rock   ┆ Omanyte             ┆ Omastar         ┆ Geodude                 │
│ Water  ┆ Slowpoke            ┆ Magikarp        ┆ Blastoise               │
│ Water  ┆ Slowbro             ┆ Tentacool       ┆ BlastoiseMega Blastoise │
│ Water  ┆ SlowbroMega Slowbro ┆ Horsea          ┆ Cloyster                │
└────────┴─────────────────────┴─────────────────┴─────────────────────────┘
```

## Flattened window function

If we have a window function that aggregates to a `list` like the example above with the following Python expression:

`pl.col("Name").sort_by(pl.col("Speed")).head(3).list().over("Type 1")`

and in Rust:

`col("Name").sort_by(["Speed"], [false]).head(Some(3)).list().over(["Type 1"])`

This still works, but that would give us a column type `List` which might not be what we want (this would significantly increase our memory usage!).

Instead we could `flatten`. This just turns our 2D list into a 1D array and projects that array/column back to our `DataFrame`.
This is very fast because the reshape is often free, and adding the column back the the original `DataFrame` is also a lot cheaper (since we don't require a join like in a normal window function).

However, for this operation to make sense, it is important that the columns used in `over([..])` are sorted!