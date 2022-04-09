# Polars Expressions

`Polars` has a powerful concept called expressions. Polars expressions can be used in
various contexts and are a functional mapping of `Fn(Series) -> Series`, meaning that they have a `Series` as an input and
a `Series` as an output. By looking at this functional definition, we can see that the output of an `Expr` also can serve
as the input of an `Expr`.

That may sound a bit strange, so let's start with an example.
