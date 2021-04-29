# How can I use custom functions?
There will always be an operation so sketchy, so dirty, so grotesque, that you cannot do with the public API of Polars.
Luckily we provide UDFs (User Defined Functions). This means you can define a python function/ lambda and pass it to the
logical plan. You can use custom functions in both the eager API as well as the lazy API. 

## Examples

Let's start with eager. Let's say we want to apply a map to a Series. This could be done as shown below.

### Eager

```python
{{#include ../examples/how_can_i/use_custom_functions.py:3:8}}
print(s.collect())
```

```text
{{#include ../outputs/how_can_i_use_custom_functions_0.txt}}
```

There are a few gotcha's however. Polars Series can only contain a single datatype. (_storing custom Python objects is being worked on_)
In the `.apply` method above we didn't specify the data type the Series should contain. Polars tries to infer the output
datatype beforehand by calling the provided function itself. If it later gets a data type that does not matched the 
initially inferred type, the value will be indicated as missing: `null`. If you already know the output datatype you need
it's recommended to provide this information to Polars.

```python
s.apply(lambda x: my_map[x], dtype_out=pl.Utf8)
```

### Lazy
In lazy you can apply custom functions via the `.map` and the `.apply` methods.
 
#### map
You can use `map` to map from a `Series` to a `Series` or a `DataFrame` to 
a `DataFrame`. 

#### apply
Or you can use `apply` to operate on the values of a `Series`. The function passed to `.apply` operate on a single primitive 
(e.g. int, str, bool).
The `lambda` we used above got `int` as input and returned `str` after finding the right key in the `dictionary`.

When a custom function is used, the output type must also be provided
because for the optimizer to be able to do optimizations the Schema of the query needs to be known at all times.

```python
{{#include ../examples/how_can_i/use_custom_functions_1.py:1:19}}
print(s.collect())
```

```text
{{#include ../outputs/how_can_i_use_custom_functions_1.txt}}
```

Above we've defined out own function, added this to the lazy query and it got executed during execution of the physical plan.
This of course greatly increases flexibility of a query and when needed you are definitely encouraged to do so. This is however
not without cost. Even though we only use vectorized code in this example (numpy functions and Polars comparisons), this query
may still be slower than a full Polars native query. This is due to the Python `GIL`. As mentioned before, polars tries to parallelize
the query execution on the available cores on your machine. However, in Python there may only be one thread modifying Python objects.
So if you have many UDF's they'd have to wait in line until they are allowed there GIL time.


### Apply
Similarly as done in the eager example, we can also `apply` a lambda over the elements of a `Series`:

```python
{{#include ../examples/how_can_i/use_custom_functions_2.py:1:15}}
print(out.collect())
```

```text
{{#include ../outputs/how_can_i_use_custom_functions_2.txt}}
```


### GroupBy

You can also use custom functions in a GroupBy context. The most intuitive way to apply custom functions is with the
`apply_groups` method. This method will receive a `Series` of every group as input. Below we'll show 3 ways the get
the length of the groups, where 2 use custom functions.

```python
{{#include ../examples/how_can_i/use_custom_functions_3.py:1:26}}
print(out.collect())
```

```text
{{#include ../outputs/how_can_i_use_custom_functions_3.txt}}
```
