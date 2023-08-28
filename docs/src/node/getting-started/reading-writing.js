const pl = require("nodejs-polars");

// --8<-- [start:dataframe]
let df = pl.DataFrame({
    integer: [1, 2, 3],
    date: [
        new Date(2022, 1, 1, 0, 0),
        new Date(2022, 1, 2, 0, 0),
        new Date(2022, 1, 3, 0, 0),
    ],
    float: [4.0, 5.0, 6.0],
});
console.log(df);
// --8<-- [end:dataframe]

// --8<-- [start:csv]
df.writeCSV("docs/data/output.csv");
var df_csv = pl.readCSV("docs/data/output.csv");
console.log(df_csv);
// --8<-- [end:csv]

// --8<-- [start:csv2]
var df_csv = pl.readCSV("docs/data/output.csv", { parseDates: true });
console.log(df_csv);
// --8<-- [end:csv2]

// --8<-- [start:json]
df.writeJSON("docs/data/output.json", { format: "json" });
let df_json = pl.readJSON("docs/data/output.json");
console.log(df_json);
// --8<-- [end:json]

// --8<-- [start:parquet]
df.writeParquet("docs/data/output.parquet");
let df_parquet = pl.readParquet("docs/data/output.parquet");
console.log(df_parquet);
// --8<-- [end:parquet]
