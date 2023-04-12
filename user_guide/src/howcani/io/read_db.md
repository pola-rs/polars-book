# Read from MySQL, Postgres, Sqlite, Redshift, Clickhouse,...

We can read from a database with the `pl.read_database` function. To use this function you need an SQL query string and a connection uri.

For example, to read all columns from the `foo` table in a Postgres database you would do the following:
```python
import polars as pl

uri = "postgres://username:password@server:port/database"
query = "SELECT * FROM foo"

pl.read_database(query=query, uri=uri)
```

## Engine
Polars doesn't handle connections and data transfer from databases by itself. Instead external libraries (known as *engines*) handle this. At present Polars can use two engines to read from databases: [connector-x](https://github.com/sfu-db/connector-x) and [ADBC](https://arrow.apache.org/docs/format/ADBC.html).

### Connector-x
Connector-x [supports numerous databases](https://github.com/sfu-db/connector-x#sources) including Postgres, Mysql, SQL Server, Redshift etc. Connector-x is written in Rust and stores data in Arrow format to allow for zero-copy to Polars. At present Connector-x is the default engine for database connections from Polars.


To read from one of the supported databases with `connector-x` it needs to be installed

```shell
$  pip install connectorx
```

### ADBC
ADBC (Arrow Database Connectivity) is supported by the Apache Arrow project and aims to be both an API standard for connecting to databases and libraries implementing this standard in a range of languages.

It is still early days for ADBC so support for different databases and data types is still limited. To install ADBC you need to install the driver for your database. For example to connect to SQLite you run

```shell
$  pip install adbc-driver-sqlite
```
At present drivers are only available for Postgres and SQLite. If this changes please feel free to [create an issue](https://github.com/pola-rs/polars-book/issues) [or pull request](https://github.com/pola-rs/polars-book/pulls) in this repository!

To use ADBC you then specify the engine as an argument to `pl.read_database`
```python
uri = "postgres://username:password@server:port/database"
query = "SELECT * FROM foo"

pl.read_database(query=query, uri=uri,engine="adbc")
```

