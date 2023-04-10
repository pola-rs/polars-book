from ..paths import OUTPUT_BASE_DIR, create_if_not_exists
from .snippet1 import q1 as q1
from .snippet1 import q1_plan as q1_plan
from .snippet1 import q1_opt_plan as q1_opt_plan
from .snippet2 import q1 as q1_snippet2
from .snippet3 import q3 as q3
from .snippet3 import q3_schema as q3_schema
from .snippet4 import q4 as q4
from .snippet5 import q5 as q5
from .snippet6 import q6 as q6
from .snippet8 import lazy_eager_query
from .snippet9 import q9
from .snippet10 import dataset
from .snippet11 import q11

path = create_if_not_exists(f"{OUTPUT_BASE_DIR}/lazy_api")

for n, x in enumerate([q1, q1_snippet2]):
    x.show_graph(optimized=False, show=False, output_path=f"{path}/graph{n + 1}.png")
    x.show_graph(optimized=True, show=False, output_path=f"{path}/graph{n + 1}-optimized.png")

df1 = q1.fetch(int(1e7))

variable_filename_tuples = [
    (q1_plan, "q1_plan"),
    (q1_opt_plan, "q1_opt_plan"),
    (dataset, "dataset"),
    (df1, "df1"),
    (q4, "df4"),
    (q5, "q5"),
    (lazy_eager_query, "lazy_eager_query"),
    (q9, "q9"),
    (q11, "q11"),
    (q3_schema, "q3_schema"),
]
for variable, filename in variable_filename_tuples:
    with open(f"{path}/{filename}.txt", "w") as f:
        f.write(f"{variable}\n")
