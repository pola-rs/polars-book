//!
//! ```cargo
//! [dependencies]
//! rand = "0.8.5"
//! polars = "0.*"
//! ```


use polars::prelude::*;
use rand::Rng;

fn main() {
    let mut rng = rand::thread_rng();

    // --8<-- [start:join]
    let df: DataFrame = df!("a" => 0..8,
                            "b"=> (0..8).map(|_| rng.gen::<f64>()).collect::<Vec<f64>>(),
                            "d"=> [Some(1.0), Some(2.0), None, None, Some(0.0), Some(-5.0), Some(-42.), None]
                        ).expect("should not fail");
    let df2: DataFrame = df!("x" => 0..8,
                            "y"=> &["A", "A", "A", "B", "B", "C", "X", "X"],
                        ).expect("should not fail");
    let joined = df.join(&df2,["a"],["x"],JoinType::Left,None).unwrap();
    println!("{}",joined);
    // --8<-- [start:join]
    
    // --8<-- [start:hstack]
    let stacked = df.hstack(df2.get_columns()).unwrap();
    println!("{}",stacked);
    // --8<-- [end:hstack]

}
