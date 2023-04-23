"""
# --8<-- [start:read]
import polars as pl

conn = "postgres://username:password@server:port/database"
query = "SELECT * FROM foo"

pl.read_sql(query, conn)
# --8<-- [end:read]
"""