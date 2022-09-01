use std::ops::Mul;

use color_eyre::Result;
use polars::prelude::*;
use rand::{thread_rng, Rng};

fn main() -> Result<()> {
    let mut arr = [0f64; 5];
    thread_rng().fill(&mut arr);
    let df = df! [
        "nrs" => [Some(1), Some(2), Some(3), None, Some(5)],
        "names" => [Some("foo"), Some("ham"), Some("spam"), Some("eggs"), None],
        "random" => arr,
        "groups" => ["A", "A", "B", "C", "B"],
    ]?;

    // ANCHOR: select
    let out = df
        .clone()
        .lazy()
        .select([
            sum("nrs"),
            col("names").sort(false),
            col("names").first().alias("first name"),
            mean("nrs").mul(lit(10)).alias("10xnrs"),
        ])
        .collect()?;
    println!("{}", out);
    // ANCHOR_END: select

    // ANCHOR: add_columns
    let out = df
        .clone()
        .lazy()
        .with_columns([
            sum("nrs").alias("nrs_sum"),
            col("random").count().alias("count"),
        ])
        .collect()?;
    println!("{}", out);
    // ANCHOR_END: add_columns

    // ANCHOR: groupby
    let out = df
        .lazy()
        .groupby([col("groups")])
        .agg([
            sum("nrs"),                           // sum nrs by groups
            col("random").count().alias("count"), // count group members
            // sum random where name != null
            col("random")
                .filter(col("names").is_not_null())
                .sum()
                .suffix("_sum"),
            col("names").reverse().alias("reversed names"),
        ])
        .collect()?;
    println!("{}", out);
    // ANCHOR_END: groupby

    Ok(())
}
