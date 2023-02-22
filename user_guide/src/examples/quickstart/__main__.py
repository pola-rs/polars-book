from ..paths import OUTPUT_BASE_DIR, create_if_not_exists
from .series_tuple import series as s1
from .series_list import series as s2
from .dataframe1 import df as df1
from .dataframe2 import df as df2
from .dataframe3 import df as df3
from .head import out as h1
from .tail import out as t1
from .sample import out as s1
from .describe import out as d1
from .select1 import out as sel1
from .select2 import out as sel2
from .select3 import out as sel3
from .select4 import out as sel4
from .filter1 import out as f1
from .filter2 import out as f2
from .withcolumns import out as wc1
from .groupby1 import out as gb1
from .groupby2 import out as gb2
from .combine1 import out as c1
from .combine2 import out as c2
from .join_df1 import df1 as j1
from .join_df2 import df2 as j2
from .qs_join1 import out as join1
from .concat1 import out as concat1

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

with open(f"{path}/select1.txt", "w") as f:
    f.write(f"{sel1}\n")

with open(f"{path}/select2.txt", "w") as f:
    f.write(f"{sel2}\n")

with open(f"{path}/select3.txt", "w") as f:
    f.write(f"{sel3}\n")

with open(f"{path}/select4.txt", "w") as f:
    f.write(f"{sel4}\n")

with open(f"{path}/filter1.txt", "w") as f:
    f.write(f"{f1}\n")

with open(f"{path}/filter2.txt", "w") as f:
    f.write(f"{f2}\n")

with open(f"{path}/withcolumns.txt", "w") as f:
    f.write(f"{wc1}\n")

with open(f"{path}/output3.csv", "w") as f:
    f.write(f"{df3}\n")

with open(f"{path}/groupby1.txt", "w") as f:
    f.write(f"{gb1}\n")

with open(f"{path}/groupby2.txt", "w") as f:
    f.write(f"{gb2}\n")

with open(f"{path}/combine1.txt", "w") as f:
    f.write(f"{c1}\n")

with open(f"{path}/combine2.txt", "w") as f:
    f.write(f"{c2}\n")

with open(f"{path}/join_df1.txt", "w") as f:
    f.write(f"{j1}\n")

with open(f"{path}/join_df2.txt", "w") as f:
    f.write(f"{j2}\n")

with open(f"{path}/qs_join1.txt", "w") as f:
    f.write(f"{join1}\n")

with open(f"{path}/concat1.txt", "w") as f:
    f.write(f"{concat1}\n")