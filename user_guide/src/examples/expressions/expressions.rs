// ANCHOR: dataset
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

    println!("{}", &df);
    // ANCHOR_END: dataset

    // ANCHOR: count_unique
    let out = df
        .clone()
        .lazy()
        .select([
            col("names").n_unique().alias("unique_names_1"),
            col("names").unique().count().alias("unique_names_2"),
        ])
        .collect()?;
    println!("{}", out);
    // ANCHOR_END: count_unique

    // ANCHOR: aggregations
    let out = df
        .clone()
        .lazy()
        .select([
            sum("random").alias("sum"),
            min("random").alias("min"),
            max("random").alias("max"),
            col("random").max().alias("other_max"),
            col("random").std(1).alias("std dev"),
            col("random").var(1).alias("variance"),
        ])
        .collect()?;
    println!("{}", out);
    // ANCHOR_END: aggregations

    // ANCHOR: conditional
    let out = df
        .clone()
        .lazy()
        .select([col("names")
            .filter(col("names").str().contains("am$"))
            .count()])
        .collect()?;
    println!("{}", out);
    // ANCHOR_END: conditional

    // ANCHOR: binary
    let out = df
        .clone()
        .lazy()
        .select([when(col("random").gt(0.5)).then(0).otherwise(col("random")) * sum("nrs")])
        .collect()?;
    println!("{}", out);
    // ANCHOR_END: binary

    // ANCHOR: window
    let df = df
        .lazy()
        .select([
            col("*"), // Select all
            col("random")
                .sum()
                .over([col("groups")])
                .alias("sum[random]/groups"),
            col("random")
                .list()
                .over([col("names")])
                .alias("random/name"),
        ])
        .collect()?;
    println!("{}", df);
    // ANCHOR_END: window

    Ok(())
}
