# Schema in the lazy API
The schema of a Polars `DataFrame` or `LazyFrame` sets out the names of the columns and their datatypes. You can see the schema with the `schema` method on a `DataFrame` or `LazyFrame` 
```python
{{#include ../examples/lazy_api/snippet3.py::6}}
```

```text
{{#include ../outputs/lazy_api/output4.txt}}
```

One advantage of the lazy API is that Polars will check your schema when you execute your lazy query but before any data is processed. 


## Operations that cannot be done in the lazy API
To use the lazy API Polars must know the schema at every step of a query plan. This means that operations where the schema is not knowable in advance can not be used with the lazy API.

The classic example of an operation where the schema is not knowable in advance is a `pivot` operation. With a `pivot` the column names come from data in one of the columns. As these data cannot be known in advance a `pivot` cannot be used in the lazy API.

If your pipeline includes an operation that cannot be done in the lazy API it is normally best to:
- run the pipeline in lazy mode up until that point
- exectute the pipeline
- do the non-lazy operation
- convert the output back to a `LazyFrame` and continue in lazy mode
