# Interact with Google BigQuery

To read or write from GBQ, additional dependencies are needed:

```shell
$ pip install google-cloud-bigquery
```

## Read

We can load a query into a `DataFrame` like this:

```python
import polars as pl
from google.cloud import bigquery

client = bigquery.Client()

# Perform a query.
QUERY = (
    'SELECT name FROM `bigquery-public-data.usa_names.usa_1910_2013` '
    'WHERE state = "TX" '
    'LIMIT 100')
query_job = client.query(QUERY)  # API request
rows = query_job.result()  # Waits for query to finish

df = pl.from_arrow(rows.to_arrow())
```

## Write

> This content is under construction.
