# --8<-- [start:setup]
import polars as pl

# --8<-- [end:setup]

# --8<-- [start:context]
ctx = pl.SQLContext()
# --8<-- [end:context]

# --8<-- [start:register_context]
df = pl.DataFrame({"a": [1, 2, 3]})
lf = pl.LazyFrame({"b": [4, 5, 6]})

# Register all dataframes in the global namespace: registers both df and lf
ctx = pl.SQLContext(register_globals=True)

# Other option: register dataframe df as "df" and lazyframe lf as "lf"
ctx = pl.SQLContext(df=df, lf=lf)
# --8<-- [end:register_context]

# --8<-- [start:register_pandas]
import pandas as pd

df_pandas = pd.DataFrame({"c": [7, 8, 9]})
ctx = pl.SQLContext(df_pandas=pl.from_pandas(df_pandas))
# --8<-- [end:register_pandas]

# --8<-- [start:execute]
# For local files use scan_csv instead
pokemon = pl.read_csv(
    "https://gist.githubusercontent.com/ritchie46/cac6b337ea52281aa23c049250a4ff03/raw/89a957ff3919d90e6ef2d34235e6bf22304f3366/pokemon.csv"
)
ctx = pl.SQLContext(register_globals=True, eager_execution=True)
df_small = ctx.execute("SELECT * from pokemon LIMIT 5")
print(df_small)
# --8<-- [start:execute]
