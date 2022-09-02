// ANCHOR: dataset
use color_eyre::Result;
use polars::prelude::*;
use reqwest::blocking::Client;

fn main() -> Result<()> {
    let data: Vec<u8> = Client::new()
        .get("https://gist.githubusercontent.com/ritchie46/cac6b337ea52281aa23c049250a4ff03/raw/89a957ff3919d90e6ef2d34235e6bf22304f3366/pokemon.csv")
        .send()?
        .text()?
        .bytes()
        .collect();

    let df = CsvReader::new(std::io::Cursor::new(data))
        .has_header(true)
        .finish()?;

    println!("{}", df);
    // ANCHOR_END: dataset

    // ANCHOR: select
    let out = df
        .clone()
        .lazy()
        .select([
            col("Type 1"),
            col("Type 2"),
            col("Attack")
                .mean()
                .over(["Type 1"])
                .alias("avg_attack_by_type"),
            col("Defense")
                .mean()
                .over(["Type 1", "Type 2"])
                .alias("avg_defense_by_type_combination"),
            col("Attack").mean().alias("avg_attack"),
        ])
        .collect()?;

    println!("{}", out);
    // ANCHOR_END: select

    // ANCHOR: filtered
    let filtered = df
        .clone()
        .lazy()
        .filter(col("Type 2").eq(lit("Psychic")))
        .select([col("Name"), col("Type 1"), col("Speed")])
        .collect()?;

    println!("{}", filtered);
    // ANCHOR_END: filtered

    // ANCHOR: discontinuous
    let out = filtered
        .lazy()
        .with_columns([cols(["Name", "Speed"]).sort(true).over(["Type 1"])])
        .collect()?;
    println!("{}", out);
    // ANCHOR_END: discontinuous

    // ANCHOR: more
    let out = df
        .clone()
        .lazy()
        .select([
            col("Type 1")
                .head(Some(3))
                .list()
                .over(["Type 1"])
                .flatten(),
            col("Name")
                .sort_by(["Speed"], [false])
                .head(Some(3))
                .list()
                .over(["Type 1"])
                .flatten()
                .alias("fastest/group"),
            col("Name")
                .sort_by(["Attack"], [false])
                .head(Some(3))
                .list()
                .over(["Type 1"])
                .flatten()
                .alias("strongest/group"),
            col("Name")
                .sort(false)
                .head(Some(3))
                .list()
                .over(["Type 1"])
                .flatten()
                .alias("sorted_by_alphabet"),
        ])
        .collect()?;
    println!("{:?}", out);
    // ANCHOR_END: more

    let df = df! [
        "foo" => [11, 22, 33, 44, 55],
        "groups" => [Some("foo"), Some("ham"), Some("spam"), Some("eggs"), None],
        "x" => [1, 2, 3, 4, 5],
        "y" => [3, 4, 5, 6, 7],
    ]?
    .lazy();

    let _temp = df
        .select([
            // ANCHOR: rules
            // aggregate and broadcast within a group
            // output type: -> i32
            sum("foo").over([col("groups")]),
            // sum within a group and multiply with group elements
            // output type: -> i32
            (col("x").sum() * col("y"))
                .over([col("groups")])
                .alias("x1"),
            // sum within a group and multiply with group elements
            // and aggregate the group to a list
            // output type: -> ChunkedArray<i32>
            (col("x").sum() * col("y"))
                .list()
                .over([col("groups")])
                .alias("x2"),
            // note that it will require an explicit `list()` call
            // sum within a group and multiply with group elements
            // and aggregate the group to a list
            // the flatten call explodes that list

            // This is the fastest method to do things over groups when the groups are sorted
            (col("x").sum() * col("y"))
                .list()
                .over([col("groups")])
                .flatten()
                .alias("x3"),
        ])
        .collect()?;
    // ANCHOR_END: rules
    Ok(())
}
