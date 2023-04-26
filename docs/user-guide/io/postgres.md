# Postgres

## Read

To read from postgres, additional dependencies are needed:

=== ":fontawesome-brands-python: Python"
    ``` shell-python
    $  pip install connectorx>=0.2.0a3
    ```

Then you can read with the following code snippet:

{{code_block('user-guide/io/postgres','read',['read_database'])}}


## Write

To write to postgres, additional dependencies are needed:


=== ":fontawesome-brands-python: Python"
    ``` shell-python
    $  pip install psycopg2-binary
    ```

For writing to a postgres database with `psycopg2`, we utilize `execute_batch`. This will limit round trips needed
to the server.

We first make sure that all our dtypes are in a format that `psycopg2` recognizes, and then we use `DataFrame.rows` to
easily transform the columnar data to rows that the database driver can work with.

{{code_block('user-guide/io/postgres','write',['read_parquet'])}}