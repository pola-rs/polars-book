# Coming from pandas

Users coming from `pandas` generally need to know one thing...

```
polars != pandas
```

If your polars code looks like it could be pandas code, it might run, but it likely runs slower than it has to be.

Let's go through some typical pandas code and see how we might write that in polars

## Column assignment

**pandas**

```python
# executes sequential
df["a"] = df["b"] * 10
df["c"] = df["b"] * 100
```

**polars**

```python
# executes in parallel
df.with_columns([
    (pl.col("b") * 10).alias("a"),
    (pl.col("b") * 100).alias("c"),
])
```

## Column asignment based on predicate

**pandas**

```python
df.loc[df["c"] == 2, "a"] = df.loc[df["c"] == 2, "b"]
```

**polars**

```python
df.with_column(
    pl.when(pl.col("c") == 2)
    .then(pl.col("b"))
    .otherwise(pl.col("a")).alias("a")
)
```

Note that polars way is pure (the original DataFrame) is not modified. The `mask` is also not computed twice as in `pandas`.
You could prevent this in `pandas`, but that would require setting a temporary variable.
Additionally polars can compute every branch of an `if -> then -> otherwise` in parallel. This is valuable, when the branches
get more expensive to compute.

## Filtering

**pandas**

```python
df.loc[(df['sqft_living'] > 2500) & (df['price'] < 300000)]
```

**polars**

```python
df.filter(
    (pl.col("m2_living") > 2500) & (pl.col("price") < 300000)
)
```

> More in redaction. Miss something? make a PR :).

## No index

They are not needed. Not having them makes things easier. Convince me otherwise

## Pandas Transform

The pandas documentation shows an operation on a groupby called `transform`. They show the following
example:

**pandas**

```python
df = pd.DataFrame({
    "c": [1, 1, 1, 2, 2, 2, 2],
    "type": ["m", "n", "o", "m", "m", "n", "n"]
})

df["size"] = df.groupby("c")["type"].transform(len)
```

Here they groupby `"c"` take `column "type"`, compute the group `len` and then join the result back to the original `DataFrame`
producing:

```
   c type size
0  1    m    3
1  1    n    3
2  1    o    3
3  2    m    4
4  2    m    4
5  2    n    4
6  2    n    4
```

**polars**

In polars the same can be achieved with `window functions`.

```python
df.select([
    pl.all(),
    pl.col("type").count().over("c").alias("size")
])
```

```
shape: (7, 3)
┌─────┬──────┬──────┐
│ c   ┆ type ┆ size │
│ --- ┆ ---  ┆ ---  │
│ i64 ┆ str  ┆ u32  │
╞═════╪══════╪══════╡
│ 1   ┆ m    ┆ 3    │
├╌╌╌╌╌┼╌╌╌╌╌╌┼╌╌╌╌╌╌┤
│ 1   ┆ n    ┆ 3    │
├╌╌╌╌╌┼╌╌╌╌╌╌┼╌╌╌╌╌╌┤
│ 1   ┆ o    ┆ 3    │
├╌╌╌╌╌┼╌╌╌╌╌╌┼╌╌╌╌╌╌┤
│ 2   ┆ m    ┆ 4    │
├╌╌╌╌╌┼╌╌╌╌╌╌┼╌╌╌╌╌╌┤
│ 2   ┆ m    ┆ 4    │
├╌╌╌╌╌┼╌╌╌╌╌╌┼╌╌╌╌╌╌┤
│ 2   ┆ n    ┆ 4    │
├╌╌╌╌╌┼╌╌╌╌╌╌┼╌╌╌╌╌╌┤
│ 2   ┆ n    ┆ 4    │
└─────┴──────┴──────┘
```

Because we can store the whole operation in a single expression we can combine several `window`functions and
even combine different groups!

Polars will cache window expression that are applied over the same group, so storing them in single `select` is not only
convenient, but also optimal.

```python
df.select([
    pl.all(),
    pl.col("c").count().over("c").alias("size"),
    pl.col("c").sum().over("type").alias("sum"),
    pl.col("c").reverse().over("c").flatten().alias("reverse_type")
])
```

```
shape: (7, 5)
┌─────┬──────┬──────┬─────┬──────────────┐
│ c   ┆ type ┆ size ┆ sum ┆ reverse_type │
│ --- ┆ ---  ┆ ---  ┆ --- ┆ ---          │
│ i64 ┆ str  ┆ u32  ┆ i64 ┆ i64          │
╞═════╪══════╪══════╪═════╪══════════════╡
│ 1   ┆ m    ┆ 3    ┆ 5   ┆ 2            │
├╌╌╌╌╌┼╌╌╌╌╌╌┼╌╌╌╌╌╌┼╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌╌╌┤
│ 1   ┆ n    ┆ 3    ┆ 5   ┆ 2            │
├╌╌╌╌╌┼╌╌╌╌╌╌┼╌╌╌╌╌╌┼╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌╌╌┤
│ 1   ┆ o    ┆ 3    ┆ 1   ┆ 2            │
├╌╌╌╌╌┼╌╌╌╌╌╌┼╌╌╌╌╌╌┼╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌╌╌┤
│ 2   ┆ m    ┆ 4    ┆ 5   ┆ 2            │
├╌╌╌╌╌┼╌╌╌╌╌╌┼╌╌╌╌╌╌┼╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌╌╌┤
│ 2   ┆ m    ┆ 4    ┆ 5   ┆ 1            │
├╌╌╌╌╌┼╌╌╌╌╌╌┼╌╌╌╌╌╌┼╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌╌╌┤
│ 2   ┆ n    ┆ 4    ┆ 5   ┆ 1            │
├╌╌╌╌╌┼╌╌╌╌╌╌┼╌╌╌╌╌╌┼╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌╌╌┤
│ 2   ┆ n    ┆ 4    ┆ 5   ┆ 1            │
└─────┴──────┴──────┴─────┴──────────────┘

```
