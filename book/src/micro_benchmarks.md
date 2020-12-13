# Micro benchmarks
Below are some micro benchmarks shown between Polars and Pandas. Note that these are just micro benchmarks and nothing
more. An optimization can lead to increased performance in a single benchmark and lead to regressions somewhere else.

To truly make performance comparisons we should at least look at the macro level of a query. 

## Csv parsing
![](img/csv.png)

# Joins
![](img/join_80_000.png)

## Groupby
![](img/groupby10_.png)
![](img/groupby10_mem.png)
