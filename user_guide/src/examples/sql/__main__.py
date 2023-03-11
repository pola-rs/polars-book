from ..paths import OUTPUT_BASE_DIR, create_if_not_exists
from .sql_1 import pokemon as sql_1
from .sql_2 import out as sql_2

path = create_if_not_exists(f"{OUTPUT_BASE_DIR}/sql")

with open(f"{path}/sql_1.txt", "w") as f:
    f.write(f"{sql_1}\n")

with open(f"{path}/sql_2.txt", "w") as f:
    f.write(f"{sql_2}\n")
