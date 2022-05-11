import json
import sys

if len(sys.argv) > 1:
    if sys.argv[1] == "supports":
        sys.exit(0)
    # sys.argv[2] is the renderer name

context, book = json.load(sys.stdin)
content = json.dumps(book)

substitutes = (
    ("POLARS_ROOT", "/polars-book/user-guide"),
    ("POLARS_RS_REF_GUIDE", "https://docs.rs/polars"),
    (
        "POLARS_PY_REF_GUIDE",
        "https://pola-rs.github.io/polars/py-polars/html/reference",
    ),
)

for old, new in substitutes:
    content = content.replace(old, new)

sys.stdout.write(content)
