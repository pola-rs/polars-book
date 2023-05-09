# --8<-- [start:setup]
import polars as pl

# --8<-- [end:setup]

# --8<-- [start:context]
sql = pl.SQLContext()
# --8<-- [end:context]


# --8<-- [start:register]
# For local files use scan_csv instead
pokemon = pl.read_csv(
    "https://gist.githubusercontent.com/ritchie46/cac6b337ea52281aa23c049250a4ff03/raw/89a957ff3919d90e6ef2d34235e6bf22304f3366/pokemon.csv"
).lazy()
sql.register("pokemon", pokemon)
df_small = sql.query("SELECT * from pokemon LIMIT 5")
print(df_small)
# --8<-- [end:register]
