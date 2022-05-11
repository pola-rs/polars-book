# IO

`Polars` supports different file types, and its respective parsers are amongst the fastest
out there.

For instance, it is faster to load a CSV file *via* `Polars` before handing it to `Pandas`
than loading them using `Pandas`. Just run a
`pl.read_csv("<FILE>", rechunk=False).to_pandas()` to convince yourself!
