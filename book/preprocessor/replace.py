#!/usr/bin/env python

import json
import sys

if len(sys.argv) > 1:
    if sys.argv[1] == "supports":
        # sys.argv[2] is the renderer name
        sys.exit(0)

context, book = json.load(sys.stdin)

preprocessor = context["config"]["preprocessor"]["replace"]

replace_token = preprocessor["replace_token"]
substitute = preprocessor["substitute"]

content = json.dumps(book)

content = content.replace(replace_token, substitute)

sys.stdout.write(content)
