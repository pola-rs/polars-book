# Read from MySQL, Postgres, Sqlite, Redshift, Clickhouse

To read from one of the supported databases `connector-x` needs to be installed.

```shell
$  pip install connectorx>=0.2.0a3
```

```python
import polars as pl

conn = "postgres://username:password@server:port/database"
query = "SELECT * FROM foo"

pl.read_sql(query, conn)
```
