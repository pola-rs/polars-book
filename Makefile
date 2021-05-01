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

run: data
	-@mkdir -p user_guide/src/_outputs
	$(PYTHON) -m user_guide.src.examples.aggregate
	$(PYTHON) -m user_guide.src.examples.conditionally_apply
	$(PYTHON) -m user_guide.src.examples.groupby
	$(PYTHON) -m user_guide.src.examples.groupby_dsl
	$(PYTHON) -m user_guide.src.examples.group_statistics
	$(PYTHON) -m user_guide.src.examples.head
	$(PYTHON) -m user_guide.src.examples.predicate_pushdown
	$(PYTHON) -m user_guide.src.examples.projection_pushdown
	$(PYTHON) -m user_guide.src.examples.strings
	$(PYTHON) -m user_guide.src.examples.strings_performance
	$(PYTHON) -m user_guide.src.examples.timestamps
	$(PYTHON) -m user_guide.src.examples.udfs
	$(PYTHON) -m user_guide.src.examples.window_functions

clean:
	-@rm -fr .venv
	-@rm -fr data
	-@rm -fr user_guide/src/_outputs
	-@rm -fr `find . -name __pycache__`
	-@cd user_guide; mdbook clean
