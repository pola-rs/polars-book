from ..paths import OUTPUT_BASE_DIR, create_if_not_exists
from .series_tuple import series as s1
from .series_list import series as s2
from .dataframe1 import df as df1
from .dataframe2 import df as df2
from .head import out as h1
from .tail import out as t1
from .sample import out as s1
from .describe import out as d1

path = create_if_not_exists(f"{OUTPUT_BASE_DIR}/quickstart")

with open(f"{path}/series_tuple.txt", "w") as f:
    f.write(f"{s1}\n")

with open(f"{path}/series_list.txt", "w") as f:
    f.write(f"{s2}\n")

with open(f"{path}/output.csv", "w") as f:
    f.write(f"{df1}\n")

with open(f"{path}/output.json", "w") as f:
    f.write(f"{df1}\n")

with open(f"{path}/output.parquet", "w") as f:
    f.write(f"{df1}\n")

with open(f"{path}/output2.csv", "w") as f:
    f.write(f"{df2}\n")

with open(f"{path}/head.txt", "w") as f:
    f.write(f"{h1}\n")

with open(f"{path}/tail.txt", "w") as f:
    f.write(f"{t1}\n")

with open(f"{path}/sample.txt", "w") as f:
    f.write(f"{s1}\n")

with open(f"{path}/describe.txt", "w") as f:
    f.write(f"{d1}\n")