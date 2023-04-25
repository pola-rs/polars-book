# Basic Operators

This section describes how to use basic operators (e.g. addition, substraction) in conjunction with Expressions. We will provide various examples using different themes in the context of the following dataframe.

!!! note Operator Overloading

    In Rust and Python it is possible to use the operators directly (as in `+ - * / < > `) as the language allows operator overloading. For instance, the operator `+` translates to the `.add()` method. In NodeJS this is not possible and you must use the methods themselves, in python and rust you can choose which one you prefer.

=== ":fontawesome-brands-python: Python"
    [:material-api:  `DataFrame`](https://pola-rs.github.io/polars/py-polars/html/reference/dataframe/index.html)
    ``` python
    --8<-- "user-guide/python/expressions/operators.py:dataframe"
    ```

```python exec="on" result="text" session="user-guide/operators"
--8<-- "user-guide/python/expressions/operators.py:setup"
--8<-- "user-guide/python/expressions/operators.py:dataframe"
```

### Numerical

=== ":fontawesome-brands-python: Python"
    [:material-api:  `operators`](https://pola-rs.github.io/polars/py-polars/html/reference/expressions/operators.html)
    ``` python
    --8<-- "user-guide/python/expressions/operators.py:numerical"
    ```

```python exec="on" result="text" session="user-guide/operators"
--8<-- "user-guide/python/expressions/operators.py:numerical"
```

### Logical

=== ":fontawesome-brands-python: Python"
    [:material-api:  `operators`](https://pola-rs.github.io/polars/py-polars/html/reference/expressions/operators.html)
    ``` python
    --8<-- "user-guide/python/expressions/operators.py:logical"
    ```

```python exec="on" result="text" session="user-guide/operators"
--8<-- "user-guide/python/expressions/operators.py:logical"
```