.DEFAULT_GOAL := help

PYTHONPATH=
SHELL=/bin/bash
VENV = .venv

ifeq ($(OS),Windows_NT)
	VENV_BIN=$(VENV)/Scripts
else
	VENV_BIN=$(VENV)/bin
endif

install-graphviz:
ifeq ($(shell uname), Darwin) # MacOS
	brew install graphviz
else ifeq ($(shell uname -o), Cygwin) # Windows
	choco install graphviz
else ifeq ($(shell uname -o), GNU/Linux) # Linux
	if command -v apt-get >/dev/null; then sudo apt-get install -y graphviz; fi
	if command -v yum >/dev/null; then sudo yum install -y graphviz; fi
	if command -v dnf >/dev/null; then sudo dnf install -y graphviz; fi
	if command -v pacman >/dev/null; then sudo pacman -S --noconfirm graphviz; fi
else
	@echo "Could not identify OS or appropriate package manager."
endif

.venv:  ## Set up virtual environment and install requirements
	python3 -m venv $(VENV)
	$(MAKE) requirements
	$(MAKE) install-graphviz

.PHONY: requirements
requirements: .venv  ## Install/refresh all project requirements
	$(VENV_BIN)/python -m pip install --upgrade pip
	$(VENV_BIN)/pip install --upgrade -r requirements.txt

.PHONY: serve
serve: .venv  ## Serve the docs locally
	$(VENV_BIN)/mkdocs serve

.PHONY: lint
lint: .venv  ## Lint code examples
# python
	$(VENV_BIN)/black --check .

.PHONY: test-python
test-python: .venv  ## Test Python code examples
	find docs/src/python -type f | xargs -n 1 bash -c '$(VENV_BIN)/python -W error $$0 || exit 255'

.PHONY: help
help:  ## Display this help screen
	@echo -e "\033[1mAvailable commands:\033[0m"
	@grep -E '^[a-z.A-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-18s\033[0m %s\n", $$1, $$2}' | sort
