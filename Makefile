SHELL=/bin/bash
PYTHON=.venv/bin/python
DATA_SRC=https://github.com/ritchie46/static/releases/download/0.0.1
DATA_DIR=data

.venv:
	@python -m venv .venv
	@.venv/bin/pip install -U pip
	@.venv/bin/pip install --no-cache-dir -r requirements.txt

serve:
	cd /usr/src/user_guide; mdbook serve --hostname 0.0.0.0 --port 8000

.PHONY: data
data: .venv
	@mkdir -p $(DATA_DIR)
	$(PYTHON) generate_data.py
	wget -q $(DATA_SRC)/reddit100k.tar.gz -O - | tar -xzf - -O > $(DATA_DIR)/reddit.csv
	wget -q $(DATA_SRC)/runescape100k.tar.gz -O - | tar -xzf - -O > $(DATA_DIR)/runescape.csv

run: #data
	-@mkdir -p user_guide/src/_outputs
	$(PYTHON) -m user_guide.src._examples.aggregate
	$(PYTHON) -m user_guide.src._examples.conditionally-apply
	$(PYTHON) -m user_guide.src._examples.groupby
	$(PYTHON) -m user_guide.src._examples.groupby-dsl
	$(PYTHON) -m user_guide.src._examples.group-statistics
	$(PYTHON) -m user_guide.src._examples.head
	$(PYTHON) -m user_guide.src._examples.predicate-pushdown
	$(PYTHON) -m user_guide.src._examples.projection-pushdown
	$(PYTHON) -m user_guide.src._examples.strings
	$(PYTHON) -m user_guide.src._examples.strings-performance
	$(PYTHON) -m user_guide.src._examples.timestamps
	$(PYTHON) -m user_guide.src._examples.udfs
	$(PYTHON) -m user_guide.src._examples.window-functions

clean:
	-@rm -fr .venv
	-@rm -fr data
	-@rm -fr user_guide/src/_outputs
	-@rm -fr `find . -name __pycache__`
	-@cd user_guide; mdbook clean
