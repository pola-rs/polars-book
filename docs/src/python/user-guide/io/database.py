f"""
# --8<-- [start:read]
import polars as pl

uri = "postgres://username:password@server:port/database"
query = "SELECT * FROM foo"

pl.read_database(query=query, uri=uri)
# --8<-- [end:read]

# --8<-- [start:adbc]
uri = "postgres://username:password@server:port/database"
query = "SELECT * FROM foo"

pl.read_database(query=query, uri=uri, engine="adbc")
# --8<-- [end:adbc]

# --8<-- [start:write]
uri = "postgres://username:password@server:port/database"
df = pl.DataFrame({"foo": [1, 2, 3]})

df.write_database(table_name="records",connection_uri=uri)
# --8<-- [end:write]

"""
