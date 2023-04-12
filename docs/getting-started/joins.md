# Combining DataFrames

There are two ways `DataFrame`s can be combined depending on the use case: join and concat.

## Join

Polars supports all types of join (e.g. left, right, inner, outer). Let's have a closer look on how to `join` two `DataFrames` into a single `DataFrame`. Our two `DataFrames` both have an 'id'-like column: `a` and `x`. We can use those columns to `join` the `DataFrames` in this example.

=== ":fontawesome-brands-python: Python"

    ``` python
    df = pl.DataFrame({"a": np.arange(0, 8), 
                    "b": np.random.rand(8), 
                    "d": [1, 2.0, np.NaN, np.NaN, 0, -5, -42, None]
                    })

    df2 = pl.DataFrame({
                        "x": np.arange(0, 8), 
                        "y": ['A', 'A', 'A', 'B', 'B', 'C', 'X', 'X'],
    })
    joined = df.join(df2, left_on="a", right_on="x")
    print(joined)
    ```

=== ":fontawesome-brands-rust: Rust"

    ``` rust
    let df: DataFrame = df!("a" => 0..8,
                            "b"=> (0..8).map(|_| rng.gen::<f64>()).collect::<Vec<f64>>(),
                            "d"=> [Some(1.0), Some(2.0), None, None, Some(0.0), Some(-5.0), Some(-42.), None]
                        ).expect("should not fail");
    let df2: DataFrame = df!("x" => 0..8,
                            "y"=> &["A", "A", "A", "B", "B", "C", "X", "X"],
                        ).expect("should not fail");
    let joined = df.join(&df2,["a"],["x"],JoinType::Left,None).unwrap();
    println!("{}",joined);
    ```
=== ":fontawesome-brands-node-js: NodeJS"

    ``` javaScript
    df = pl.DataFrame({"a": [...Array(8).keys()], 
                    "b": Array.from({length: 8}, () => Math.random()), 
                    "d": [1, 2.0, null, null, 0, -5, -42, null]
                    })

    df2 = pl.DataFrame({
                        "x": [...Array(8).keys()], 
                        "y": ['A', 'A', 'A', 'B', 'B', 'C', 'X', 'X'],
    })
    joined = df.join(df2, {leftOn:"a", rightOn:"x"})
    console.log(joined);
    ```

```
shape: (8, 4)
┌─────┬──────────┬───────┬─────┐
│ a   ┆ b        ┆ d     ┆ y   │
│ --- ┆ ---      ┆ ---   ┆ --- │
│ f64 ┆ f64      ┆ f64   ┆ str │
╞═════╪══════════╪═══════╪═════╡
│ 0.0 ┆ 0.568449 ┆ 1.0   ┆ A   │
├╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌┼╌╌╌╌╌┤
│ 1.0 ┆ 0.252443 ┆ 2.0   ┆ A   │
├╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌┼╌╌╌╌╌┤
│ 2.0 ┆ 0.708543 ┆ null  ┆ A   │
├╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌┼╌╌╌╌╌┤
│ 3.0 ┆ 0.08118  ┆ null  ┆ B   │
├╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌┼╌╌╌╌╌┤
│ 4.0 ┆ 0.449587 ┆ 0.0   ┆ B   │
├╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌┼╌╌╌╌╌┤
│ 5.0 ┆ 0.443502 ┆ -5.0  ┆ C   │
├╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌┼╌╌╌╌╌┤
│ 6.0 ┆ 0.434625 ┆ -42.0 ┆ X   │
├╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌┼╌╌╌╌╌┤
│ 7.0 ┆ 0.372544 ┆ null  ┆ X   │
└─────┴──────────┴───────┴─────┘

```

## Concat

We can also `concatenate` two `DataFrames`. Vertical concatenation will make the `DataFrame` longer. Horizontal concatenation will make the `DataFrame` wider. Below you can see the result of an horizontal concatenation of our two `DataFrames`.

=== ":fontawesome-brands-python: Python"

    ``` python
    stacked = df.hstack(df2) 
    print(stacked)
    ```

=== ":fontawesome-brands-rust: Rust"

    ``` rust
    let stacked = df.hstack(df2.get_columns()).unwrap();
    println!("{}",stacked);
    ```
=== ":fontawesome-brands-node-js: NodeJS"

    ``` javaScript
    stacked = df.hstack(df2);
    console.log(stacked);
    ```

```
shape: (8, 5)
┌─────┬──────────┬───────┬─────┬─────┐
│ a   ┆ b        ┆ d     ┆ x   ┆ y   │
│ --- ┆ ---      ┆ ---   ┆ --- ┆ --- │
│ f64 ┆ f64      ┆ f64   ┆ f64 ┆ str │
╞═════╪══════════╪═══════╪═════╪═════╡
│ 0.0 ┆ 0.568449 ┆ 1.0   ┆ 0.0 ┆ A   │
├╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌┼╌╌╌╌╌┼╌╌╌╌╌┤
│ 1.0 ┆ 0.252443 ┆ 2.0   ┆ 1.0 ┆ A   │
├╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌┼╌╌╌╌╌┼╌╌╌╌╌┤
│ 2.0 ┆ 0.708543 ┆ null  ┆ 2.0 ┆ A   │
├╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌┼╌╌╌╌╌┼╌╌╌╌╌┤
│ 3.0 ┆ 0.08118  ┆ null  ┆ 3.0 ┆ B   │
├╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌┼╌╌╌╌╌┼╌╌╌╌╌┤
│ 4.0 ┆ 0.449587 ┆ 0.0   ┆ 4.0 ┆ B   │
├╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌┼╌╌╌╌╌┼╌╌╌╌╌┤
│ 5.0 ┆ 0.443502 ┆ -5.0  ┆ 5.0 ┆ C   │
├╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌┼╌╌╌╌╌┼╌╌╌╌╌┤
│ 6.0 ┆ 0.434625 ┆ -42.0 ┆ 6.0 ┆ X   │
├╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌┼╌╌╌╌╌┼╌╌╌╌╌┤
│ 7.0 ┆ 0.372544 ┆ null  ┆ 7.0 ┆ X   │
└─────┴──────────┴───────┴─────┴─────┘

```