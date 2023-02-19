# Schema in the lazy API

The schema of a Polars `DataFrame` or `LazyFrame` sets out the names of the columns and their datatypes. You can see the schema with the `schema` method on a `DataFrame` or `LazyFrame`

```python
{{#include ../examples/lazy_api/snippet3.py::6}}
```

```text
{{#include ../outputs/lazy_api/output4.txt}}
```

The schema plays an important role in the lazy API.

## Type checking in the lazy API

One advantage of the lazy API is that when you execute your lazy query Polars will check your schema before any data is processed.

To illustrate this we take the following simple where example we call the `round` expression on the `bar` column.

```python
{{#include ../examples/lazy_api/snippet7.py}}
```

The problem is that the `bar` column has an integer dtype and the `round` expression is only valid for columns with a floating point dtype. This means the operation will raise a `SchemaError`.

If we executed this query in eager mode the error would only be found once the data had been processed in all earlier steps.

When we execute a lazy query Polars checks for any potential `SchemaError` before the time-consuming step of actually processing the data in the pipeline.

## The lazy API must know the schema

In the lazy API the Polars query optimizer must be able to infer the schema at every step of a query plan. This means that operations where the schema is not knowable in advance cannot be used with the lazy API.

The classic example of an operation where the schema is not knowable in advance is a `pivot` operation. In a `pivot` the new column names come from data in one of the columns. As these column names cannot be known in advance a `pivot` is not available in the lazy API.

## Dealing with operations not available in the lazy API

If your pipeline includes an operation that cannot be done in the lazy API it is normally best to:

- run the pipeline in lazy mode up until that point
- execute the pipeline with `collect` to materialize a `DataFrame`
- do the non-lazy operation on the `DataFrame`
- convert the output back to a `LazyFrame` with `.lazy` and continue in lazy mode

We show how to deal with a non-lazy operation in this example where we:

- enter into lazy mode to get a `LazyFrame`
- do a transformation using `with_columns`
- execute the query before the `pivot` with `collect` to get a `DataFrame`
- do the `pivot` on the `DataFrame`
- enter back into lazy mode
- do a `filter`
- finish by executing the query with `collect` to get a `DataFrame`

```python
{{#include ../examples/lazy_api/snippet8.py}}
```

```text
{{#include ../outputs/lazy_api/q8.txt}}
```
