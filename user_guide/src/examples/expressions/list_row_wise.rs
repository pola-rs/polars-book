use color_eyre::Result;
use polars::prelude::*;

fn main() -> Result<()> {
    // ANCHOR: dataset
    let grades = df![
        "student" => ["bas", "laura", "tim", "jenny"],
        "arithmetic" => [10, 5, 6, 8],
        "biology" => [4, 6, 2, 7],
        "geography" => [8, 4, 9, 7],
    ]?;
    println!("{}", grades);
    // ANCHOR_END: dataset

    // ANCHOR: row-wise
    let out = grades
        .clone()
        .lazy()
        .select([concat_lst([all().exclude(["student"])]).alias("all_grades")])
        .collect()?;
    println!("{}", out);
    // ANCHOR_END: row-wise

    // ANCHOR: expressions
    // the percentage rank expression
    let rank_opts = RankOptions {
        method: RankMethod::Average,
        descending: true,
    };
    let rank_pct = col("").rank(rank_opts) / col("").count().cast(DataType::Float32);

    let grades = grades
        .clone()
        .lazy()
        .with_column(
            // create the list of homogeneous data
            concat_lst([all().exclude(["student"])]).alias("all_grades"),
        )
        .select([
            // select all columns except the intermediate list
            all().exclude(["all_grades"]),
            // compute the rank by calling `arr.eval`
            col("all_grades")
                .arr()
                .eval(rank_pct, true)
                .alias("grades_rank"),
        ])
        .collect()?;
    println!("{}", grades);
    // ANCHOR_END: expressions

    Ok(())
}
