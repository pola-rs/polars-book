# Static schemas

Do you know that feeling, you are 20 mins in a ETL job and bam, your pipeline fails because we assumed to have another
data type for a column? With polars' lazy API we know the data type and column name for any node in the pipeline.

This is very valuable information and can be used to ensure data integrity at any node in the pipeline.

```python
{{#include ../examples/testing/schema_assert.py:6:19}}
```
