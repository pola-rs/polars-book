# Contributing to the `Polars` User Guide

We love your input! We want to make contributing to this project as easy and transparent as possible, whether it is:

- Reporting a bug.
- Discussing the current state of the code.
- Submitting a fix.
- Adding/proposing new features.

## General guide

### We develop with Github

We use GitHub to host code, to track issues and feature requests, as well as accept pull requests.

1. Fork the [repo](https://github.com/pola-rs/polars-book.git) in your own GitHub account.
1. Clone your own version of the repo locally, and `cd` into it.
1. Add the upstream remote with `git remote add upstream https://github.com/pola-rs/polars-book.git`
1. All branches should derive from `master`, you can `git checkout -b <YOUR-BRANCH>` and write away.
1. Commit/push to your own repo.
1. Open a pull request as you would usually do, making sure the "base repository" is the upstream repo (`master` branch) and the "head repository" your own (`<YOUR-BRANCH>` branch).

To update your own repo with code pushed on the upstream repo:

1. `git checkout <BRANCH>`
1. `git pull upstream <BRANCH>`
1. `git push origin <BRANCH>`

A few rules:

- Ensure the examples are added to the `Makefile`.
- Make sure your code lints.

### Want to discuss something?

Some questions will not fit an issue.
For those we have [the Discord server](https://discord.gg/RhCg7uQCjQ).

### All contributions are under the MIT Software License

When contributing any content your submissions are understood to be under the same [MIT License](http://choosealicense.com/licenses/mit/) that covers the project.
Feel free to contact the maintainers if that is a concern.

### Report bugs using GitHub Issues

Do not hesitate to [open a new issue](https://github.com/pola-rs/polars-book/issues/new/choose).
**Great Issues** tend to have:

- A quick summary and/or background.
- Steps to reproduce.
- What you expected would happen.
- What actually happens.
- Notes (possibly including why you think this might be happening, or stuff you tried that did not work).

### Content formatting

The `Python` code is checked and linted using [`black`](https://github.com/psf/black), [`flake8`](https://gitlab.com/pycqa/flake8) and [`isort`](https://pycqa.github.io/isort/).
The `Markdown` files are formatted using [`mdformat`](https://github.com/executablebooks/mdformat).
The recommended way is to use [`pre-commit`](https://pre-commit.com/) before commiting your code:

```shell
$ pip install pre-commit
$ pre-commit install  # config stored in the .pre-commit-config.yaml
$ pre-commit run --all-files
```

Another way is to run each manually:

```shell
$ black .
$ flake8 --max-doc-length=88 .  # max-line-length is imposed by black
$ mdformat --wrap=88 user_guide/src/references.md
```

for instance (check the linter package versions in the `.pre-commit-config.yaml`).

## Code examples

Each time the User Guide is built, all examples are run against the latest release of `Polars` (as defined in the `requirements.txt` file found at the root of this repo).
To document a new functionality:

### *How can I?* page

The description of the code example should be placed within the *How can I?* section of the book, in the `user_guide/src/howcani/` folder.
The `Markdown` file should roughly match the following structure:

1. A clear title (for example: "*Interact with an AWS bucket*").
1. A one-ish-liner to introduce the code snippet.
1. The code example itself, included using the `{{#include .../examples/<MODULE>}}` syntax.
1. The output of the example, if applicable (follow the same syntax to include the file).
1. A longer explanation if required.
1. If applicable, provide both eager and lazy examples.

````text
# Do this

## Eager API

The code snippet below allows to do...

```python
{{#include .../examples/template/snippet.py}}
```

returning:

```text
{{#include .../outputs/template/output.py}}
```

On line 3 we can see that...

## Lazy API

Using the lazy approach presented below one can...
````

### Snippet

Each code example should:

- Run as an independent `Python` module.
- Find itself in its own folder within the `user_guide/src/examples/...` directory.
- Write any output to a file within the `user_guide/src/outputs/...` directory (under the same folder-tree).
- Be registered in the `run` recipe of the `Makefile` present at the root of the repo.

For instance, the core of an example without any extras:

```python
# user_guide/src/examples/template/lazy.py
import polars as pl

dataset = pl.scan_csv("path.csv")
df = dataset.fetch()
```

If there are multiple steps to your example, split them in separate modules.
Writing to an output file, or any other step required but not needed in the code snippet showcasing the functionality:

```python
# user_guide/src/examples/template/__main__.py
from .snippet import df
from ..paths import OUTPUT_BASE_DIR, create_if_not_exists

path = create_if_not_exists(f"{OUTPUT_BASE_DIR}/template")

with open(f"{path}/output.txt") as f:
    f.write(f"{df}\n")
```

Simply importing the `snippet.py` in the `__main__.py` module will ensure that it is ran.
Including the content of any file to the `Markdown` is done through the `{{#include user_guide/src/examples/template/snippet.py}}` (for instance) syntax.
Finally, registering the example in the `Makefile` to make sure it is tested next time the User Guide is built:

```makefile
# Makefile

run: data
	# [...]
	$(PYTHON) -m user_guide.src.examples.template
```

(Note this is pointing to the folder name; this will work only if a `__main__.py` file is present.)
Check the code snippets themselves in the `user_guide/src/examples/` folder for more inspiration.
