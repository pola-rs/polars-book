from .projection_pushdown_0 import joined
import sys

optimize = sys.argv[1] == "True"
joined.fetch(int(1e7), projection_pushdown=optimize, predicate_pushdown=optimize)
