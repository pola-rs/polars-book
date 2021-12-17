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
df[df["c"] == 2, "a"] = df[df["c"] == 2, "b"]
```

**polars**

```python
df.with_column(
    pl.when(pl.col("c") == 2)
    .then(pl.col("c"))
    .otherwise(pl.col("a")).alias("a")
)
```

Not that polars way is pure (the original DataFrame) is not modified. The `mask` is also not computed twice as in `pandas`.
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
