# Interact with Postgres

To read/write form postgres, additional dependencies are needed:

```shell
$ pip install psycopg2-binary
```

## Read

> In redaction

## Write

For writing to a postgres database with `psycopg2`, we utilize `execute_batch`. This will limit the needed round trips
to the server.

We first make sure that all our dtypes are in a format that `psycopg2` recognizes, and then we use `DataFrame.rows` to
easily transform the columnar data to rows that the database driver can work with.

```python
from psycopg2 import sql
import psycopg2.extras
import polars as pl

# let's assume we have a DataFrame with some floats, integers, strings, and date64 columns.
df = pl.read_parquet("somefile.parquet")

# first me convert polars date64 representation to python datetime objects 
for col in df:
    # only for date64
    if col.dtype == pl.Date64:
        df = df.with_column(col.dt.to_python_datetime())

# create sql identifiers for the column names
# we do this to safely insert this into a sql query
columns = sql.SQL(",").join(sql.Identifier(name) for name in df.columns)

# create placeholders for the values. These will be filled later
values = sql.SQL(",").join([sql.Placeholder() for _ in df.columns])

table_id = "mytable"

# prepare the insert query
insert_stmt = sql.SQL("INSERT INTO ({}) VALUES({});").format(
    sql.Identifier(table_id), columns, values
)

# make a connection
conn = psycopg2.connect()
cur = conn.cursort()

# do the insert
psycopg2.extras.execute_batch(cur, insert_stmt, df.rows())
conn.commit()
```
