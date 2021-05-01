# IO

Polars support different file types and its respective parsers are amongst the fastest out there.

For instance, it is faster to load a CSV file *via* `Polars` before handing it `Pandas`, than directly using `Pandas`.
(Just run a `pl.read_csv("<FILE>", rechunk=False).to_pandas()` to convince yourself.)

