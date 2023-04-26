# Database

To read from one of the supported databases (e.g. MySQL, Postgres, Sqlite, Redshift, Clickhouse)`connector-x` needs to be installed.

=== ":fontawesome-brands-python: Python"
    ``` shell-python
    $  pip install connectorx>=0.2.0a3
    ```

Then you can read using the `read_databse` function:

{{code_block('user-guide/io/database','read',['read_database'])}}

