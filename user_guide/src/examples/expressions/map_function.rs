use color_eyre::Result;
use polars::prelude::*;

fn main() -> Result<()> {
    let df = df! [
        "keys" => ["a", "a", "b"],
        "values" => [10, 7, 1],
    ]?;

    let out = df
        .lazy()
        .groupby(["keys"])
        .agg([
            col("values")
                .map(|s| Ok(s.shift(1)), GetOutput::default())
                .alias("shift_map"),
            col("values").shift(1).alias("shift_expression"),
        ])
        .collect()?;

    println!("{}", out);

    Ok(())
}
