# CSV

## Read & Write

Reading a CSV file should look familiar:

=== ":fontawesome-brands-python: Python"
    ``` python
    --8<-- "user-guide/python/io/csv.py:read"
    ```

Writing a CSV file is similar with the `write_csv` function:

=== ":fontawesome-brands-python: Python"
    ``` python
    --8<-- "user-guide/python/io/csv.py:write"
    ```

## Scan

`Polars` allows you to *scan* a CSV input. Scanning delays the actual parsing of the
file and instead returns a lazy computation holder called a `LazyFrame`.

=== ":fontawesome-brands-python: Python"
    ``` python
    --8<-- "user-guide/python/io/csv.py:scan"
    ```

If you want to know why this is desirable, you can read more about those `Polars`
optimizations [here](../concepts/lazy-vs-eager.md).
