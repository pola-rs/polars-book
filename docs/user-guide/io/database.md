# Read from a database

We can read from a database with Polars using the `pl.read_database` function. To use this function you need an SQL query string and a connection string called a `uri`.

For example, the following snippet shows the general patterns for reading all columns from the `foo` table in a Postgres database:

{{code_block('user-guide/io/database','read',['read_database'])}}

## Engines

Polars doesn't manage connections and data transfer from databases by itself. Instead external libraries (known as *engines*) handle this. At present Polars can use two engines to read from databases: [connector-x](https://github.com/sfu-db/connector-x) and [ADBC](https://arrow.apache.org/docs/format/ADBC.html).

### Connector-x

Connector-x is the default engine and [supports numerous databases](https://github.com/sfu-db/connector-x#sources) including Postgres, Mysql, SQL Server and Redshift. Connector-x is written in Rust and stores data in Arrow format to allow for zero-copy to Polars.

To read from one of the supported databases with `connector-x` you need to install it

```shell
$  pip install connectorx
```

### ADBC

ADBC (Arrow Database Connectivity) is an engine supported by the Apache Arrow project. ADBC aims to be both an API standard for connecting to databases and libraries implementing this standard in a range of languages.

It is still early days for ADBC so support for different databases is still limited. At present drivers for ADBC are only available for [Postgres and SQLite](https://arrow.apache.org/adbc/0.1.0/driver/cpp/index.html). To install ADBC you need to install the driver for your database. For example to install the driver for SQLite you run

```shell
$  pip install adbc-driver-sqlite
```

AS ADBC is not the default enginee you must specify the engine as an argument to `pl.read_database`

{{code_block('user-guide/io/database','adbc',['read_database'])}}


