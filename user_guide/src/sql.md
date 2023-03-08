# Polars SQL

## Starting the SQL Context

You can query a `Polars` `LazyFrame` with SQL. 
The first step is to initialize a SQL context, and register a `LazyFrame` with it.

Let's load some data and initialize the SQL context:

```python
import polars as pl

# convert 'pokemon' into a Lazyframe by calling the .lazy() method 
pokemon = pl.read_csv(
    "https://gist.githubusercontent.com/ritchie46/cac6b337ea52281aa23c049250a4ff03/raw/89a957ff3919d90e6ef2d34235e6bf22304f3366/pokemon.csv"
).lazy()

# initialize the SQL context and register the lazyframe
sql = pl.SQLContext()
sql.register('pokemon', pokemon)

```

Polars supports a single SQL context per thread, and the registered dataframe should be a `LazyFrame`.
You can call the register function multiple time for each of your LazyFrame.

## Running your SQL queries 🚀🚀

You run your SQL queries with `SQLContext.query`.

```python
sql.query("""
SELECT 
    "Type 1",
    COUNT(DISTINCT "Type 2") AS count_type_2,
    AVG(Attack) AS avg_attack_by_type,
    MAX(Speed) AS max_speed
FROM pokemon
GROUP BY "Type 1"
""")

shape: (15, 4)
┌────────┬──────────────┬────────────────────┬───────────┐
│ Type 1 ┆ count_type_2 ┆ avg_attack_by_type ┆ max_speed │
│ ---    ┆ ---          ┆ ---                ┆ ---       │
│ str    ┆ u32          ┆ f64                ┆ i64       │
╞════════╪══════════════╪════════════════════╪═══════════╡
│ Dragon ┆ 2            ┆ 94.0               ┆ 80        │
│ Fire   ┆ 3            ┆ 88.642857          ┆ 105       │
│ ...    ┆ ...          ┆ ...                ┆ ...       │
│ Rock   ┆ 3            ┆ 87.5               ┆ 150       │
│ Fairy  ┆ 1            ┆ 57.5               ┆ 60        │
│ Ice    ┆ 2            ┆ 67.5               ┆ 95        │
└────────┴──────────────┴────────────────────┴───────────┘
```

## Available SQL functions

### Math functions

- `ABS`: Compute the absolute values.
- `ACOS`: Compute the element-wise value for the cosine.
- `ASIN`: Compute the element-wise value for the sine.
- `ATAN`: Compute the element-wise value for the tangent.
- `CEIL` or `CEILING`: Rounds up to the nearest integer value. Only works on floating point Series.
- `EXP`: Compute the exponential, element-wise.
- `FLOOR`: Rounds down to the nearest integer value. Only works on floating point Series.
- `LN`: Compute the logarithm in base n.
- `LOG2`: Compute the logarithm in base 2.
- `LOG10`: Compute the logarithm in base 10.
- `LOG`: Compute the logarithm in a given base.
- `POW`: Raise expression to the power of exponent.

### String functions

- `LOWER`: Transform to lowercase variant.
- `UPPER`: Transform to uppercase variant.
- `LTRIM`: Remove leading characters.
- `RTRIM`: Remove trailing characters.
- `STARTS_WITH`: Check if string values start with a substring.
- `ENDS_WITH`: Check if string values end with a substring.

### Aggregate functions

- `COUNT`: Count the number of values in this expression.
- `SUM`: Get sum value.
- `MIN`: Get minimum value.
- `MAX`: Get maximum value.
- `AVG`: Get mean value.
- `STDDEV` or `STDDEV_SAMP`: Get standard deviation.
- `VARIANCE` or `VAR_SAMP`: Get variance.
- `FIRST`: Get the first value.
- `LAST`: Get the last value.

### Array functions

- `ARRAY_LENGTH`: Get the length of the arrays as UInt32.
- `ARRAY_LOWER`: Compute the min value of the lists in the array.
- `ARRAY_UPPER`: Compute the max value of the lists in the array.
- `ARRAY_SUM`: Sum all the lists in the array.
- `ARRAY_MEAN`: Compute the mean value of the lists in the array.
- `ARRAY_REVERSE`: Reverse the arrays in the list.
- `ARRAY_UNIQUE`: Get the unique/distinct values in the list.
- `UNNEST`: Returns a column with a separate row for every list element.
- `ARRAY_GET`: Get the value by index in the sublists.
- `ARRAY_CONTAINS`: Check if sublists contain the given item.

