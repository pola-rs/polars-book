use color_eyre::{Result};
use polars::prelude::*;

fn main() -> Result<()> {

let df = df![
    "a" => [1, 2, 3],
    "b" => [10, 20, 30],
]?;

let out = df.lazy().select(&[
    fold_exprs(lit(0), |acc, x| Ok(&acc + &x), [col("*")]).alias("sum")
]).collect()?;
println!("{:?}", out);

let df = df![
    "a" => [1, 2, 3],
    "b" => [0, 1, 2],
]?;

let out = df.lazy().filter(
    fold_exprs(
        lit(true),
        |acc, x| Ok(acc.bitand(&x)?),
        [col("*").gt(1)]
    ),
).collect()?;
println!("{:?}", out);

let df = df![
    "a" => ["a", "b", "c"],
    "b" => [1, 2, 3],
]?;

let out = df.lazy().select(
    [
        
        concat_str([col("a"), col("b")], ""),
    ]
).collect()?;
println!("{:?}", out);

    Ok(())
}