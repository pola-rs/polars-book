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
    (pl.col("b") * 100).alias("b"),
])
```

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
