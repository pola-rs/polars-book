#!/bin/bash

set -e

# if not on gh-pages brach exit
git status | grep gh-pages

echo '<meta http-equiv=refresh content=0;url=book/book/index.html>' > index.html
rm -r book/src
rm .gitignore
echo '.venv/' > .gitignore
echo '.idea/' >> .gitignore
echo 'data/' >> .gitignore
echo '__pychache__/' >> .gitignore



