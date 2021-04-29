# How can I conditionally apply

You often want to modify or add a column to DataFrame based on some condition/predicate. This is where
the `when().then().otherwise()` expressions are for. As they are basically a full English sentence, they need no further
explanation.


## Examples

```python
{{#include ../examples/how_can_i/conditionally_apply.py:1:10}}
print(out.collect())
```

```text
{{#include ../outputs/how_can_i_conditionally_apply.txt}}
```
