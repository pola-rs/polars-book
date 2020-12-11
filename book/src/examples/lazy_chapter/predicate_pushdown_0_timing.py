from .predicate_pushdown_0 import reddit
import sys

reddit.fetch(int(1e7), predicate_pushdown=sys.argv[1] == "True")
