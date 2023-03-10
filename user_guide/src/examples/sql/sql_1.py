import polars as pl

# convert 'pokemon' into a Lazyframe by calling the .lazy() method
pokemon = pl.read_csv(
    "https://gist.githubusercontent.com/ritchie46/cac6b337ea52281aa23c049250a4ff03/raw/89a957ff3919d90e6ef2d34235e6bf22304f3366/pokemon.csv"
).lazy()

# initialize the SQL context and register the lazyframe
sql = pl.SQLContext()
sql.register("pokemon", pokemon)
