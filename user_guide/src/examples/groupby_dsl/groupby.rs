use color_eyre::Result;
use polars::prelude::*;
use reqwest::blocking::Client;
use std::io::Cursor;

fn main() -> Result<()> {
    // ANCHOR: dataset
    let url = "https://theunitedstates.io/congress-legislators/legislators-historical.csv";

    let mut schema = Schema::new();
    schema.with_columns("first_name".to_string(), DataType::Categorical(None));
    schema.with_columns("gender".to_string(), DataType::Categorical(None));
    schema.with_columns("type".to_string(), DataType::Categorical(None));
    schema.with_columns("state".to_string(), DataType::Categorical(None));
    schema.with_columns("party".to_string(), DataType::Categorical(None));
    schema.with_columns("birthday".to_string(), DataType::Date);

    let data: Vec<u8> = Client::new().get(url).send()?.text()?.bytes().collect();

    let dataset = CsvReader::new(Cursor::new(data))
        .has_header(true)
        .with_dtypes(Some(&schema))
        .with_parse_dates(true)
        .finish()?;

    println!("{}", &dataset);
    // ANCHOR_END: dataset

    // ANCHOR: aggregation
    let df = dataset
        .clone()
        .lazy()
        .groupby(["first_name"])
        .agg([count(), col("gender").list(), col("last_name").first()])
        .sort(
            "count",
            SortOptions {
                descending: true,
                nulls_last: true,
            },
        )
        .limit(5)
        .collect()?;

    println!("{}", df);
    // ANCHOR_END: aggregation

    // ANCHOR: conditional
    let df = dataset
        .clone()
        .lazy()
        .groupby(["state"])
        .agg([
            (col("party").eq(lit("Anti-Administration")))
                .sum()
                .alias("anti"),
            (col("party").eq(lit("Pro-Administration")))
                .sum()
                .alias("pro"),
        ])
        .sort(
            "pro",
            SortOptions {
                descending: true,
                nulls_last: false,
            },
        )
        .limit(5)
        .collect()?;

    println!("{}", df);
    // ANCHOR_END: conditional

    // ANCHOR: nested_groupby
    let df = dataset
        .clone()
        .lazy()
        .groupby(["state", "party"])
        .agg([col("party").count().alias("count")])
        .filter(
            col("party")
                .eq(lit("Anti-Administration"))
                .or(col("party").eq(lit("Pro-Administration"))),
        )
        .sort(
            "count",
            SortOptions {
                descending: true,
                nulls_last: true,
            },
        )
        .limit(5)
        .collect()?;

    println!("{}", df);
    // ANCHOR_END: nested_groupby

    // ANCHOR: filtering
    fn compute_age() -> Expr {
        lit(2022) - col("birthday").dt().year()
    }

    fn avg_birthday(gender: &str) -> Expr {
        compute_age()
            .filter(col("gender").eq(lit(gender)))
            .mean()
            .alias(&format!("avg {} birthday", gender))
    }

    let df = dataset
        .clone()
        .lazy()
        .groupby(["state"])
        .agg([
            avg_birthday("M"),
            avg_birthday("F"),
            (col("gender").eq(lit("M"))).sum().alias("# male"),
            (col("gender").eq(lit("F"))).sum().alias("# female"),
        ])
        .limit(5)
        .collect()?;

    println!("{}", df);
    // ANCHOR_END: filtering

    // ANCHOR: sorting1
    fn get_person() -> Expr {
        col("first_name") + lit(" ") + col("last_name")
    }

    let df = dataset
        .clone()
        .lazy()
        .sort(
            "birthday",
            SortOptions {
                descending: true,
                nulls_last: true,
            },
        )
        .groupby(["state"])
        .agg([
            get_person().first().alias("youngest"),
            get_person().last().alias("oldest"),
        ])
        .limit(5)
        .collect()?;

    println!("{}", df);
    // ANCHOR_END: sorting1

    // ANCHOR: sorting2
    let df = dataset
        .clone()
        .lazy()
        .sort(
            "birthday",
            SortOptions {
                descending: true,
                nulls_last: true,
            },
        )
        .groupby(["state"])
        .agg([
            get_person().first().alias("youngest"),
            get_person().last().alias("oldest"),
            get_person().sort(false).first().alias("alphabetical_first"),
        ])
        .limit(5)
        .collect()?;

    println!("{}", df);
    // ANCHOR_END: sorting2

    // ANCHOR: sorting3
    let df = dataset
        .clone()
        .lazy()
        .sort(
            "birthday",
            SortOptions {
                descending: true,
                nulls_last: true,
            },
        )
        .groupby(["state"])
        .agg([
            get_person().first().alias("youngest"),
            get_person().last().alias("oldest"),
            get_person().sort(false).first().alias("alphabetical_first"),
            col("gender")
                .sort_by(["first_name"], [false])
                .first()
                .alias("gender"),
        ])
        .sort("state", SortOptions::default())
        .limit(5)
        .collect()?;

    println!("{}", df);
    // ANCHOR_END: sorting3

    Ok(())
}
