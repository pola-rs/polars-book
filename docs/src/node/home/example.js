// --8<-- [start:example]
const pl = require("nodejs-polars");

q = pl
  .scanCSV("docs/data/iris.csv")
  .filter(pl.col("sepal_length").gt(5))
  .groupBy("species")
  .agg(pl.all().sum());

df = q.collect();
// --8<-- [end:example]
