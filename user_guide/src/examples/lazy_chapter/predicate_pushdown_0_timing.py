import sys

from .predicate_pushdown_0 import reddit

reddit.fetch(int(1e7), predicate_pushdown=sys.argv[1] == "True")
