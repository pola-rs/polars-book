use polars::prelude::*;

fn main() -> Result<(), Box<dyn std::error::Error>> {
    // --8<-- [start:selectors_df]

    use chrono::prelude::*;
    use polars::time::*;

    let df = df!(
            "id" => &[9, 4, 2],
            "place" => &["Mars", "Earth", "Saturn"],
        "date" => date_range("date",
			    NaiveDate::from_ymd_opt(2022, 1, 1).unwrap().and_hms_opt(0, 0, 0).unwrap(), NaiveDate::from_ymd_opt(2022, 1, 3).unwrap().and_hms_opt(0, 0, 0).unwrap(), Duration::parse("1d"),ClosedWindow::Both, TimeUnit::Milliseconds, None)?,
            "sales" => &[33.4, 2142134.1, 44.7],
            "has_people" => &[false, true, false],
            "logged_at" => date_range("logged_at",
			    NaiveDate::from_ymd_opt(2022, 1, 1).unwrap().and_hms_opt(0, 0, 0).unwrap(), NaiveDate::from_ymd_opt(2022, 1, 1).unwrap().and_hms_opt(0, 0, 2).unwrap(), Duration::parse("1s"),ClosedWindow::Both, TimeUnit::Milliseconds, None)?,
    )?
    .with_row_count("rn", None)?;
    println!("{}", &df);
    // --8<-- [end:selectors_df]

    // --8<-- [start:all]
    let out = df.clone().lazy().select([col("*")]).collect()?;

    // Is equivalent to
    let out = df.clone().lazy().select([all()]).collect()?;
    println!("{}", &out);
    // --8<-- [end:all]

    // --8<-- [start:exclude]
    let out = df
        .clone()
        .lazy()
        .select([col("*").exclude(["logged_at", "rn"])])
        .collect()?;
    println!("{}", &out);
    // --8<-- [end:exclude]

    // --8<-- [start:expansion_by_names]
    let out = df
        .clone()
        .lazy()
        .select([cols(["date", "logged_at"]).dt().to_string("%Y-%h-%d")])
        .collect()?;
    println!("{}", &out);
    // --8<-- [end:expansion_by_names]

    // --8<-- [start:expansion_by_regex]
    let out = df.clone().lazy().select([col("^.*(as|sa).*$")]).collect()?;
    println!("{}", &out);
    // --8<-- [end:expansion_by_regex]

    // --8<-- [start:expansion_by_dtype]
    let out = df
        .clone()
        .lazy()
        .select([dtype_cols([DataType::Int64, DataType::UInt32, DataType::Boolean]).n_unique()])
        .collect()?;
    // gives different result than python as the id col is i32 in rust
    println!("{}", &out);
    // --8<-- [end:expansion_by_dtype]

    Ok(())
}
