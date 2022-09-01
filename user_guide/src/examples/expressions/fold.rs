use color_eyre::Result;
use polars::prelude::*;

fn main() -> Result<()> {
    // ANCHOR: manual_sum
    let df = df![
        "a" => [1, 2, 3],
        "b" => [10, 20, 30],
    ]?;

    let out = df
        .lazy()
        .select([fold_exprs(lit(0), |acc, x| Ok(acc + x), [col("*")]).alias("sum")])
        .collect()?;
    println!("{}", out);
    // ANCHOR_END: manual_sum

    // ANCHOR: conditional
    let df = df![
        "a" => [1, 2, 3],
        "b" => [0, 1, 2],
    ]?;

    let out = df
        .lazy()
        .filter(fold_exprs(
            lit(true),
            |acc, x| acc.bitand(&x),
            [col("*").gt(1)],
        ))
        .collect()?;
    println!("{}", out);
    // ANCHOR_END: conditional

    // ANCHOR: string
    let df = df![
        "a" => ["a", "b", "c"],
        "b" => [1, 2, 3],
    ]?;

    let out = df
        .lazy()
        .select([concat_str([col("a"), col("b")], "")])
        .collect()?;
    println!("{:?}", out);
    // ANCHOR_END: string

    Ok(())
}
