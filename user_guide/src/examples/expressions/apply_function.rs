use color_eyre::{Result};
use polars::prelude::*;

fn main() -> Result<()> {

let df = df! [
    "keys" => ["a", "a", "b"],
    "values" => [10, 7, 1],
]?;

println!("{:?}", &df);

let out = df.clone().lazy()
    .groupby([col("keys")])
    .agg([
        col("values")
            .apply(|s| Ok(s.shift(1)), GetOutput::default())
            .alias("shift_map"),
        col("values").shift(1).alias("shift_expression"),
    ])
    .collect()?;

println!("{:?}", out);

let out = df.clone().lazy()
    .select([
        as_struct(&[col("keys"), col("values")])
            .apply(|x| Ok(x.["keys"].len() + x["values"]), GetOutput::default())
            .alias("solution_apply"),
        (col("keys")/*.str().lengths()*/ + col("values")).alias("solution_expr"),
    ])
    .collect()?;

println!("{:?}", out);

    Ok(())
}
