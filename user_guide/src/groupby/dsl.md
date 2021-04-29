# GroupBy DSL

_Note that this fresh! this is currently available on any polars version >= `0.7.6-beta.2`_

In the introduction on previous page we discussed that using custom Python functions, killed parallelization, and
that we can use the DSL of the lazy API to mitigate this. Let's take a look at what that means.

## Eager and Lazy
For groupby operations you can use the lazy API in Polars eager. That means that if you run this snippet of code

```python
(df.groupby("foo")
 .agg([col("bar").sum()]))
```

It actually desugars to:

```python
(df.lazy().groupby("foo")
 .agg([col("bar").sum()]))
 .collect()
```

That means you don't have to go to lazy by yourself if you need the more powerful API.

## Why would you want this.
As discussed earlier, this allows us to delay the need of grabbing Python `lambdas` to do a more complex aggregation.
So let's start very simple and see how we can use the DSL to do increasingly complex queries.

Let's start with a simple dataset [US congress dataset](https://github.com/unitedstates/congress-legislators).

```python
{{#include ../examples/groupby/dsl.py:1:14}}
```

### Basic aggregations

You can easily combine different aggregations by adding multiple expressions in a `list`. There is no upper bound on the
number of aggregations you can do, and you can make any combination you want. 
In the snippet below we do the following aggregations:

Per GROUP `"first_name"` we

* count the number of rows in the group:
  - short form: `pl.count("party")`
  - full form: `col("party").count()`
* aggregate the gender values group to a list:
  - full form: `col("gender").list()`
* get the first value of column `"last_name"` in the group:
  - short form: `pl.first("last_name")`
  - full form: `col("last_name").first()`
  
Besides the aggregation, we immediately sort the result and limit to the top 5 so that we have a nice summary overview.

```python
{{#include ../examples/groupby/dsl.py:15:22}}

print(q.collect())
```

```text
{{#include ../outputs/groupby_dsl_0.txt}}
```

### Conditionals
Ok, that was pretty easy right. Let turn it up a notch. Let's say we want to know how many delegates of a "state" are 
"Pro" or "Anti" administration we could directly query that in the aggregation without the need of `lambda` or grooming
the DataFrame.


```python
{{#include ../examples/groupby/dsl.py:23:34}}

print(q1.collect())
```
```text
{{#include ../outputs/groupby_dsl_1.txt}}
```

Something similar could of course also be done with a nested GROUPBY, but that would not allow me showing these nice features. 😉

```python
{{#include ../examples/groupby/dsl.py:36:45}}

print(q2.collect())
```
```text
{{#include ../outputs/groupby_dsl_2.txt}}
```

### Filtering
We can also filter the groups. Let's say we want to compute a mean per group, but we don't want to include all values
from that group and we also don't want to filter the rows from the `DataFrame` (because we need that rows for another aggregation.)

In the example below we show how that can be done. Note that we can make `Python` functions for clarity. These functions 
don't cost us anything. That is because we only create `Polars` expression, we don't apply a custom function over `Series`
during runtime of the query.


```python
{{#include ../examples/groupby/dsl.py:48:80}}

print(q3.collect())
```
```text
{{#include ../outputs/groupby_dsl_3.txt}}
```


### Sorting

I often see a DataFrame being sorted for the sole purpose of the ordering during the GROUPBY operation.
Let's say that we want to get the names of the oldest and youngest (not that they are still alive) politicians per state, 
we could SORT and GROUPBY.


```python
{{#include ../examples/groupby/dsl.py:83:98}}

print(q4.collect())
```
```text
{{#include ../outputs/groupby_dsl_4.txt}}
```


However, IF we also want to sort the names alphabetically (and why wouldn't you!), this breaks. Luckily we can sort in a 
groupby context separate from the `DataFrame`.


```python
{{#include ../examples/groupby/dsl.py:100:112}}

print(q5.collect())
```
```text
{{#include ../outputs/groupby_dsl_5.txt}}
```

We can even sort by another column in the GROUPBY context. If we want to know if the alphabetically sorted name is male or
female we could add `col("gender").sort_by("first_name").first().alias("gender")`


```python
{{#include ../examples/groupby/dsl.py:114:128}}

print(q6.collect())
```
```text
{{#include ../outputs/groupby_dsl_6.txt}}
```

## Conclusion

In the examples above we've seen that we can do a lot by combining expressions. By doing so we delay the use of custom python
functions that slow down the queries (by the slow nature of Python AND the GIL).

If you think there is a type expression missing, let me know and open a [feature request](https://github.com/ritchie46/polars/issues/new/choose).
