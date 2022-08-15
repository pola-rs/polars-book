use std::io::Cursor;
use color_eyre::{Result};
use polars::prelude::*;
use reqwest::blocking::Client;

fn main() -> Result<()> { 
    let url = "https://theunitedstates.io/congress-legislators/legislators-historical.csv";

    let mut schema = Schema::new();
    schema.with_column("first_name".to_string(), DataType::Categorical(None));
    schema.with_column("gender".to_string(), DataType::Categorical(None));
    schema.with_column("type".to_string(), DataType::Categorical(None));
    schema.with_column("state".to_string(), DataType::Categorical(None));
    schema.with_column("party".to_string(), DataType::Categorical(None));

    let data: Vec<u8> = Client::new()
        .get(url)
        .send()?
        .text()?
        .bytes()
        .collect();

    let dataset = CsvReader::new(Cursor::new(data))
        .has_header(true)
        .with_dtypes(Some(&schema))
        // .with_columns(Some(vec![&"birthday"]))
        .with_parse_dates(true)
        .finish()?;

    println!("{:?}", &dataset);

    let df = dataset.clone().lazy()
        .groupby(&"first_name")
        .agg([
            count(),
            col("gender").list(),
            first("last_name"),
        ])
        .sort("count", true)
        .limit(5)
        .collect();

    println!("{:?}", df);

    Ok(())
}