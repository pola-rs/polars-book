"""
# --8<-- [start:read]
import polars as pl

uri = "postgres://username:password@server:port/database"
query = "SELECT * FROM foo"

pl.read_database(query=query, uri=uri)
# --8<-- [end:read]

# --8<-- [start:adbc]
uri = "postgres://username:password@server:port/database"
query = "SELECT * FROM foo"

pl.read_database(query=query, uri=uri,engine="adbc")
# --8<-- [end:adbc]
"""
