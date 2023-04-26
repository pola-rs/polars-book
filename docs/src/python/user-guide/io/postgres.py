"""
# --8<-- [start:read]
import polars as pl

conn = "postgresql://username:password@server:port/database"
query = "SELECT * FROM foo"

pl.read_database(query, conn)
# --8<-- [end:read]

# --8<-- [start:write]
from psycopg2 import sql
import psycopg2.extras
import polars as pl

# let's assume we have a DataFrame with some floats, integers, strings, and date64 columns.
df = pl.read_parquet("somefile.parquet")

# first me convert polars date64 representation to python datetime objects 
for col in df:
    # only for date64
    if col.dtype == pl.Date64:
        df = df.with_columns(col.dt.to_python_datetime())

# create sql identifiers for the column names
# we do this to safely insert this into a sql query
columns = sql.SQL(",").join(sql.Identifier(name) for name in df.columns)

# create placeholders for the values. These will be filled later
values = sql.SQL(",").join([sql.Placeholder() for _ in df.columns])

table_id = "mytable"

# prepare the insert query
insert_stmt = sql.SQL("INSERT INTO {} ({}) VALUES({});").format(
    sql.Identifier(table_id), columns, values
)

# make a connection
conn = psycopg2.connect()
cur = conn.cursor()

# do the insert
psycopg2.extras.execute_batch(cur, insert_stmt, df.rows())
conn.commit()
# --8<-- [end:write]
"""
