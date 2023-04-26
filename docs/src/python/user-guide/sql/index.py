# --8<-- [start:df]
import polars as pl

# convert 'pokemon' into a Lazyframe by calling the .lazy() method
pokemon = pl.read_csv(
    "https://gist.githubusercontent.com/ritchie46/cac6b337ea52281aa23c049250a4ff03/raw/89a957ff3919d90e6ef2d34235e6bf22304f3366/pokemon.csv"
).lazy()

# initialize the SQL context and register the lazyframe
sql = pl.SQLContext()
sql.register("pokemon", pokemon)
# --8<-- [end:df]

# --8<-- [start:query]
out = sql.query(
    """
SELECT 
    "Type 1",
    COUNT(DISTINCT "Type 2") AS count_type_2,
    AVG(Attack) AS avg_attack_by_type,
    MAX(Speed) AS max_speed
FROM pokemon
GROUP BY "Type 1"
"""
)
print(out)
# --8<-- [end:query]
