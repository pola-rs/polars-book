#!/usr/bin/env bash

NBPATH=./user_guide/src/notebooks

# Give the name of the jupyter notebook without the extension
# this function will convert to a python file and run it to validate its correctness
# then it will create a markdown file that can be rendered in the book
function process_nbook {
	.venv/bin/jupyter nbconvert --to python "$NBPATH/$1.ipynb"
	.venv/bin/python "$NBPATH/$1.py"
	.venv/bin/jupyter nbconvert --to markdown "$NBPATH/$1.ipynb"
}

"$@"
