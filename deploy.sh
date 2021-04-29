#!/bin/bash

# if not on the gh-pages branch exit
set -e
git status | grep gh-pages

# cleanup
rm -r .gitignore user_guide/src
echo data > .gitignore
echo __pychache__ >> .gitignore
echo .idea >> .gitignore
echo .venv >> .gitignore

echo "<meta http-equiv=refresh content=0;url=user_guide/book/index.html>" > index.html
