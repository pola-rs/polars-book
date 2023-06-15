use polars::prelude::*;

fn main() -> Result<(), Box<dyn std::error::Error>> {

    // --8<-- [start:weather_df]
    let weather = df!(
        "Station" => &[
        "Station 1", "Station 2",
        "Station 3", "Station 4",
        "Station 5"],
        "Temperatures" => &[
        "20 5 5 E1 7 13 19 9 6 20",
        "18 8 16 11 23 E2 8 E2 E2 E2 90 70 40",
        "19 24 E9 16 6 12 10 22",
        "E2 E0 15 7 8 10 E1 24 17 13 6",
        "14 8 E0 16 22 24 E1"]
    )?;
    println!("{}", weather);
    // --8<-- [end:weather_df]
    
    // --8<-- [start:string_to_list]
    // to do
    // --8<-- [end:string_to_list]

    // --8<-- [start:explode_to_atomic]
    // to do
    // --8<-- [end:explode_to_atomic]
    
    // --8<-- [start:list_ops]
    // to do
    // --8<-- [end:list_ops]

    // --8<-- [start:count_errors]
    // to do
    // --8<-- [end:count_errors]

    // --8<-- [start:count_errors_regex]
    // to do
    // --8<-- [end:count_errors_regex]

    // --8<-- [start:weather_by_day]
    // to do
    // --8<-- [end:weather_by_day]

    // --8<-- [start:weather_by_day_rank]
    // to do
    // --8<-- [end:weather_by_rank]

    // --8<-- [start:array_df]
    // to do
    // --8<-- [end:array_df]

}