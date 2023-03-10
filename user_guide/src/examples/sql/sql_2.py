import polars as pl
from .sql_1 import pokemon, sql

pl.Config.set_tbl_rows(6)

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
