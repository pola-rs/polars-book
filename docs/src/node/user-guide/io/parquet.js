// --8<-- [start:setup]
const pl = require("nodejs-polars");
// --8<-- [end:setup]

`
// --8<-- [start:read]
df = pl.readParquet("docs/data/path.parquet")
// --8<-- [end:read]
`;

// --8<-- [start:write]
df = pl.DataFrame({ foo: [1, 2, 3], bar: [null, "bak", "baz"] });
df.writeParquet("docs/data/path.parquet");
// --8<-- [end:write]

// --8<-- [start:scan]
df = pl.scanParquet("docs/data/path.parquet");
// --8<-- [end:scan]
