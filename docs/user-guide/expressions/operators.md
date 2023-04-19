# Basic Operators

This section describes how to use basic operators (e.g. addition, substraction) in conjunction with Expressions. We will provide various examples using different themes in the context of the following dataframe.

!!! note Operator Overloading

    In Rust and Python it is possible to use the operators directly (as in `+ - * / < > `) as the language allows operator overloading. For instance, the operator `+` translates to the `.add()` method. In NodeJS this is not possible and you must use the methods themselves, in python and rust you can choose which one you prefer.

=== ":fontawesome-brands-python: Python"
    ``` python
    --8<-- "user-guide/python/expressions/operators.py:dataframe"
    ```

```
shape: (5, 4)
┌──────┬───────┬──────────┬────────┐
│ nrs  ┆ names ┆ random   ┆ groups │
│ ---  ┆ ---   ┆ ---      ┆ ---    │
│ i64  ┆ str   ┆ f64      ┆ str    │
╞══════╪═══════╪══════════╪════════╡
│ 1    ┆ foo   ┆ 0.154163 ┆ A      │
│ 2    ┆ ham   ┆ 0.74005  ┆ A      │
│ 3    ┆ spam  ┆ 0.263315 ┆ B      │
│ null ┆ egg   ┆ 0.533739 ┆ C      │
│ 5    ┆ null  ┆ 0.014575 ┆ B      │
└──────┴───────┴──────────┴────────┘
```

### Numerical

=== ":fontawesome-brands-python: Python"
    ``` python
    --8<-- "user-guide/python/expressions/operators.py:numerical"
    ```

```
shape: (5, 4)
┌─────────┬─────────┬──────────────┬──────────────┐
│ nrs + 5 ┆ nrs - 5 ┆ nrs * random ┆ nrs / random │
│ ---     ┆ ---     ┆ ---          ┆ ---          │
│ i64     ┆ i64     ┆ f64          ┆ f64          │
╞═════════╪═════════╪══════════════╪══════════════╡
│ 6       ┆ -4      ┆ 0.154163     ┆ 6.486647     │
│ 7       ┆ -3      ┆ 1.480099     ┆ 2.702521     │
│ 8       ┆ -2      ┆ 0.789945     ┆ 11.393198    │
│ null    ┆ null    ┆ null         ┆ null         │
│ 10      ┆ 0       ┆ 0.072875     ┆ 343.054056   │
└─────────┴─────────┴──────────────┴──────────────┘
```

### Logical

=== ":fontawesome-brands-python: Python"
    ``` python
    --8<-- "user-guide/python/expressions/operators.py:logical"
    ```

```
shape: (5, 6)
┌─────────┬─────────────┬──────────┬──────────┬──────────┬─────────┐
│ nrs > 1 ┆ random < .5 ┆ nrs != 1 ┆ nrs == 1 ┆ and_expr ┆ or_expr │
│ ---     ┆ ---         ┆ ---      ┆ ---      ┆ ---      ┆ ---     │
│ bool    ┆ bool        ┆ bool     ┆ bool     ┆ bool     ┆ bool    │
╞═════════╪═════════════╪══════════╪══════════╪══════════╪═════════╡
│ false   ┆ true        ┆ false    ┆ true     ┆ false    ┆ true    │
│ true    ┆ false       ┆ true     ┆ false    ┆ false    ┆ true    │
│ true    ┆ true        ┆ true     ┆ false    ┆ true     ┆ true    │
│ null    ┆ false       ┆ true     ┆ false    ┆ false    ┆ null    │
│ true    ┆ true        ┆ true     ┆ false    ┆ true     ┆ true    │
└─────────┴─────────────┴──────────┴──────────┴──────────┴─────────┘
```

### 