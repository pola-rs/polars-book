# Aggregation

`Polars` implements a powerful syntax defined not only in its lazy API, but also in its eager API. Let's take a look at what that means.

We can start with the simple [US congress `dataset`](https://github.com/unitedstates/congress-legislators).


=== ":fontawesome-brands-python: Python"
    ``` python
    --8<-- "user-guide/python/expressions/aggregation.py:dataframe"
    ```

#### Basic aggregations

You can easily combine different aggregations by adding multiple expressions in a
`list`. There is no upper bound on the number of aggregations you can do, and you can
make any combination you want. In the snippet below we do the following aggregations:

Per GROUP `"first_name"` we

- count the number of rows in the group:
  - short form: `pl.count("party")`
  - full form: `pl.col("party").count()`
- aggregate the gender values groups:
  - full form: `pl.col("gender")`
- get the first value of column `"last_name"` in the group:
  - short form: `pl.first("last_name")` (not available in Rust)
  - full form: `pl.col("last_name").first()`

Besides the aggregation, we immediately sort the result and limit to the top `5` so that
we have a nice summary overview.

=== ":fontawesome-brands-python: Python"
    ``` python
    --8<-- "user-guide/python/expressions/aggregation.py:basic"
    ```

```
shape: (5, 4)
┌────────────┬───────┬───────────────────┬───────────┐
│ first_name ┆ count ┆ gender            ┆ last_name │
│ ---        ┆ ---   ┆ ---               ┆ ---       │
│ cat        ┆ u32   ┆ list[cat]         ┆ str       │
╞════════════╪═══════╪═══════════════════╪═══════════╡
│ John       ┆ 1256  ┆ ["M", "M", … "M"] ┆ Walker    │
│ William    ┆ 1022  ┆ ["M", "M", … "M"] ┆ Few       │
│ James      ┆ 714   ┆ ["M", "M", … "M"] ┆ Armstrong │
│ Thomas     ┆ 454   ┆ ["M", "M", … "M"] ┆ Tucker    │
│ Charles    ┆ 439   ┆ ["M", "M", … "M"] ┆ Carroll   │
└────────────┴───────┴───────────────────┴───────────┘
```

#### Conditionals

It's that easy! Let's turn it up a notch. Let's say we want to know how
many delegates of a "state" are "Pro" or "Anti" administration. We could directly query
that in the aggregation without the need of `lambda` or grooming the `DataFrame`.

=== ":fontawesome-brands-python: Python"
    ``` python
    --8<-- "user-guide/python/expressions/aggregation.py:conditional"
    ```

```text
shape: (5, 3)
┌───────┬──────┬─────┐
│ state ┆ anti ┆ pro │
│ ---   ┆ ---  ┆ --- │
│ cat   ┆ u32  ┆ u32 │
╞═══════╪══════╪═════╡
│ CT    ┆ 0    ┆ 3   │
│ NJ    ┆ 0    ┆ 3   │
│ NC    ┆ 1    ┆ 2   │
│ VA    ┆ 3    ┆ 1   │
│ SC    ┆ 0    ┆ 1   │
└───────┴──────┴─────┘
```

Similarly,  this could also be done with a nested GROUPBY, but that doesn't help show off some of these nice features. 😉

=== ":fontawesome-brands-python: Python"
    ``` python
    --8<-- "user-guide/python/expressions/aggregation.py:nested"
    ```

```
shape: (5, 3)
┌───────┬─────────────────────┬───────┐
│ state ┆ party               ┆ count │
│ ---   ┆ ---                 ┆ ---   │
│ cat   ┆ cat                 ┆ u32   │
╞═══════╪═════════════════════╪═══════╡
│ CT    ┆ Pro-Administration  ┆ 3     │
│ VA    ┆ Anti-Administration ┆ 3     │
│ NJ    ┆ Pro-Administration  ┆ 3     │
│ NC    ┆ Pro-Administration  ┆ 2     │
│ VA    ┆ Pro-Administration  ┆ 1     │
└───────┴─────────────────────┴───────┘
```

#### Filtering

We can also filter the groups. Let's say we want to compute a mean per group, but we
don't want to include all values from that group, and we also don't want to filter the
rows from the `DataFrame` (because we need those rows for another aggregation).

In the example below we show how that can be done.

!!! note
     Note that we can make `Python` functions for clarity. These functions don't cost us anything. That is because we only create `Polars` expressions, we don't apply a custom function over a `Series` during runtime of the query.  Of course, you can make functions that return expressions in Rust, too.

=== ":fontawesome-brands-python: Python"
    ``` python
    --8<-- "user-guide/python/expressions/aggregation.py:filter"
    ```

```text
shape: (5, 5)
┌───────┬────────────────┬────────────────┬────────┬──────────┐
│ state ┆ avg M birthday ┆ avg F birthday ┆ # male ┆ # female │
│ ---   ┆ ---            ┆ ---            ┆ ---    ┆ ---      │
│ cat   ┆ f64            ┆ f64            ┆ u32    ┆ u32      │
╞═══════╪════════════════╪════════════════╪════════╪══════════╡
│ DE    ┆ 181.593407     ┆ null           ┆ 97     ┆ 0        │
│ VA    ┆ 191.542781     ┆ 65.2           ┆ 430    ┆ 5        │
│ SC    ┆ 183.018349     ┆ 121.8          ┆ 247    ┆ 5        │
│ MD    ┆ 187.280899     ┆ 93.375         ┆ 298    ┆ 8        │
│ PA    ┆ 179.724846     ┆ 91.857143      ┆ 1050   ┆ 7        │
└───────┴────────────────┴────────────────┴────────┴──────────┘
```

#### Sorting

It's common to see a `DataFrame` being sorted for the sole purpose of managing the ordering during a GROUPBY operation. Let's say that we want to get the names of the oldest and youngest politicians per state. We could SORT and GROUPBY.

=== ":fontawesome-brands-python: Python"
    ``` python
    --8<-- "user-guide/python/expressions/aggregation.py:sort"
    ```

```
shape: (5, 3)
┌───────┬────────────────┬───────────────────┐
│ state ┆ youngest       ┆ oldest            │
│ ---   ┆ ---            ┆ ---               │
│ cat   ┆ str            ┆ str               │
╞═══════╪════════════════╪═══════════════════╡
│ DE    ┆ John Carney    ┆ Samuel White      │
│ VA    ┆ Scott Taylor   ┆ William Grayson   │
│ SC    ┆ Joe Cunningham ┆ Ralph Izard       │
│ MD    ┆ Frank Kratovil ┆ Benjamin Contee   │
│ PA    ┆ Conor Lamb     ┆ Thomas Fitzsimons │
└───────┴────────────────┴───────────────────┘
```

However, **if** we also want to sort the names alphabetically, this breaks. Luckily we can sort in a `groupby` context separate from the `DataFrame`.

=== ":fontawesome-brands-python: Python"
    ``` python
    --8<-- "user-guide/python/expressions/aggregation.py:sort2"
    ```

```
shape: (5, 4)
┌───────┬────────────────┬───────────────────┬────────────────────┐
│ state ┆ youngest       ┆ oldest            ┆ alphabetical_first │
│ ---   ┆ ---            ┆ ---               ┆ ---                │
│ cat   ┆ str            ┆ str               ┆ str                │
╞═══════╪════════════════╪═══════════════════╪════════════════════╡
│ DE    ┆ John Carney    ┆ Samuel White      ┆ Albert Polk        │
│ VA    ┆ Scott Taylor   ┆ William Grayson   ┆ A. McEachin        │
│ SC    ┆ Joe Cunningham ┆ Ralph Izard       ┆ Abraham Nott       │
│ MD    ┆ Frank Kratovil ┆ Benjamin Contee   ┆ Albert Blakeney    │
│ PA    ┆ Conor Lamb     ┆ Thomas Fitzsimons ┆ Aaron Kreider      │
└───────┴────────────────┴───────────────────┴────────────────────┘
```

We can even sort by another column in the `groupby` context. If we want to know if the alphabetically sorted name is male or female we could add: `pl.col("gender").sort_by("first_name").first().alias("gender")`

=== ":fontawesome-brands-python: Python"
    ``` python
    --8<-- "user-guide/python/expressions/aggregation.py:sort3"
    ```

```
shape: (5, 5)
┌───────┬────────────────┬───────────────────┬────────────────────┬────────┐
│ state ┆ youngest       ┆ oldest            ┆ alphabetical_first ┆ gender │
│ ---   ┆ ---            ┆ ---               ┆ ---                ┆ ---    │
│ cat   ┆ str            ┆ str               ┆ str                ┆ cat    │
╞═══════╪════════════════╪═══════════════════╪════════════════════╪════════╡
│ DE    ┆ John Carney    ┆ Samuel White      ┆ Albert Polk        ┆ M      │
│ VA    ┆ Scott Taylor   ┆ William Grayson   ┆ A. McEachin        ┆ M      │
│ SC    ┆ Joe Cunningham ┆ Ralph Izard       ┆ Abraham Nott       ┆ M      │
│ MD    ┆ Frank Kratovil ┆ Benjamin Contee   ┆ Albert Blakeney    ┆ M      │
│ PA    ┆ Conor Lamb     ┆ Thomas Fitzsimons ┆ Aaron Kreider      ┆ M      │
└───────┴────────────────┴───────────────────┴────────────────────┴────────┘
```

### Do not kill parallelization

!!! warning "Python Users Only"

    The following section is specific to `Python`, and doesn't apply to `Rust`. Within `Rust`, blocks and closures (lambdas) can, and will, be executed concurrently.

We have all heard that `Python` is slow, and does "not scale." Besides the overhead of
running "slow" bytecode, `Python` has to remain within the constraints of the Global
Interpreter Lock (GIL). This means that if you were to use a `lambda` or a custom `Python`
function to apply during a parallelized phase, `Polars` speed is capped running `Python`
code preventing any multiple threads from executing the function.

This all feels terribly limiting, especially because we often need those `lambda` functions in a
`.groupby()` step, for example. This approach is still supported by `Polars`, but
keeping in mind bytecode **and** the GIL costs have to be paid. It is recommended to try to solve your queries using the expression syntax before moving to `lambdas`.


### Conclusion

In the examples above we've seen that we can do a lot by combining expressions. By doing so we delay the use of custom `Python` functions that slow down the queries (by the slow nature of Python AND the GIL).

If we are missing a type expression let us know by opening a
[feature request](https://github.com/pola-rs/polars/issues/new/choose)!