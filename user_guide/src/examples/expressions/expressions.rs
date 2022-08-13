use color_eyre::{Result};
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
    ]?.lazy();

    println!("{:?}", df.clone().collect());

    let names = df.clone().select([
        col("names").n_unique().alias("unique_names_1"),
        col("names").unique().count().alias("unique_names_2"),
    ]).collect()?;

    println!("{:?}", names);

    let aggregations = df.clone().select([
        sum("random").alias("sum"),
        min("random").alias("min"),
        max("random").alias("max"),
        col("random").max().alias("other_max"),
        col("random").std().alias("std dev"),
        col("random").var().alias("variance"),
    ]).collect()?;

    println!("{:?}", aggregations);
    
    let am_names = df.clone().select([
        col("names").filter(col("names").str().contains("am$")).count()
    ]).collect();

    println!("{:?}", am_names);

    let randoms = df.clone().select([
        when(col("random").gt(0.5)).then(0).otherwise(col("random")) * sum("nrs"),
    ]).collect()?;
    
    println!("{:?}", randoms);

    let df = df.select([
        col("*"), // Select all
        col("random").sum().over([col("groups")]).alias("sum[random]/groups"),
        col("random").list().over([col("names")]).alias("random/name"),
    ]).collect()?;

    println!("{:?}", df);

    Ok(())
}