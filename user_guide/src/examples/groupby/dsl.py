import polars as pl
from polars import col

url = "https://theunitedstates.io/congress-legislators/legislators-historical.csv"
dtypes = {
    "first_name": pl.Categorical,
    "gender": pl.Categorical,
    "type": pl.Categorical,
    "state": pl.Categorical,
    "party": pl.Categorical,
}

df = pl.read_csv(url, dtype=dtypes)

q = (
    df.lazy()
    .groupby("first_name")
    .agg([pl.count("party"), col("gender").list(), pl.first("last_name")])
    .sort("party_count", reverse=True)
    .limit(5)
)

q1 = (
    df.lazy()
    .groupby("state")
    .agg(
        [
            (col("party") == "Anti-Administration").sum().alias("anti"),
            (col("party") == "Pro-Administration").sum().alias("pro"),
        ]
    )
    .sort("pro", reverse=True)
    .limit(5)
)

q2 = (
    df.lazy()
    .groupby(["state", "party"])
    .agg([pl.count("party").alias("count")])
    .filter(
        (col("party") == "Anti-Administration") | (col("party") == "Pro-Administration")
    )
    .sort("count", reverse=True)
    .limit(5)
)


from datetime import datetime


def compute_age() -> pl.Expr:
    # Date64 is time in ms
    ms_to_year = 1e3 * 3600 * 24 * 365
    return (
        pl.lit(datetime(2021, 1, 1)) - col("birthday").str_parse_date(pl.Date32)
    ) / (ms_to_year)


def avg_birthday(gender: str) -> pl.Expr:
    return (
        compute_age()
        .filter(col("gender") == gender)
        .mean()
        .alias(f"avg {gender} birthday")
    )


q3 = (
    df.lazy()
    .groupby(["state"])
    .agg(
        [
            avg_birthday("M"),
            avg_birthday("F"),
            (col("gender") == "M").sum().alias("# male"),
            (col("gender") == "F").sum().alias("# female"),
        ]
    )
    .limit(5)
)


def get_person() -> pl.Expr:
    return col("first_name") + pl.lit(" ") + col("last_name")


q4 = (
    df.lazy()
    .sort("birthday")
    .groupby(["state"])
    .agg(
        [
            get_person().first().alias("youngest"),
            get_person().last().alias("oldest"),
        ]
    )
    .limit(5)
)

q5 = (
    df.lazy()
    .sort("birthday")
    .groupby(["state"])
    .agg(
        [
            get_person().first().alias("youngest"),
            get_person().last().alias("oldest"),
            get_person().sort().first().alias("alphabetical_first"),
        ]
    )
    .limit(5)
)

q6 = (
    df.lazy()
    .sort("birthday")
    .groupby(["state"])
    .agg(
        [
            get_person().first().alias("youngest"),
            get_person().last().alias("oldest"),
            get_person().sort().first().alias("alphabetical_first"),
            col("gender").sort_by("first_name").first().alias("gender"),
        ]
    )
    .sort("state")
    .limit(5)
)

if __name__ == "__main__":
    out = q.collect()
    with open("user_guide/src/outputs/groupby_dsl_0.txt", "w") as f:
        f.write(str(out))

    out = q1.collect()
    with open("user_guide/src/outputs/groupby_dsl_1.txt", "w") as f:
        f.write(str(out))

    out = q2.collect()
    with open("user_guide/src/outputs/groupby_dsl_2.txt", "w") as f:
        f.write(str(out))

    out = q3.collect()
    with open("user_guide/src/outputs/groupby_dsl_3.txt", "w") as f:
        f.write(str(out))

    out = q4.collect()
    with open("user_guide/src/outputs/groupby_dsl_4.txt", "w") as f:
        f.write(str(out))

    out = q5.collect()
    with open("user_guide/src/outputs/groupby_dsl_5.txt", "w") as f:
        f.write(str(out))

    out = q6.collect()
    with open("user_guide/src/outputs/groupby_dsl_6.txt", "w") as f:
        f.write(str(out))
