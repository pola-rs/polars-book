SHELL=/bin/bash
PYTHON=.venv/bin/python
DATA_SRC=https://github.com/ritchie46/static/releases/download/0.0.1
DATA_DIR=data

.venv:
	@python -m venv .venv
	@.venv/bin/pip install -U pip
	@.venv/bin/pip install --no-cache-dir -r requirements.txt

data: .venv
	@mkdir -p $(DATA_DIR)
	$(PYTHON) generate_data.py
	wget -q $(DATA_SRC)/reddit100k.tar.gz -O - | tar -xzf - -O > $(DATA_DIR)/reddit.csv
	wget -q $(DATA_SRC)/runescape100k.tar.gz -O - | tar -xzf - -O > $(DATA_DIR)/runescape.csv

run: data
	./tasks.sh process_nbook introduction_polars
	$(PYTHON) -m user_guide.src.examples.multiple_files
	$(PYTHON) -m user_guide.src.examples.time_series
	$(PYTHON) -m user_guide.src.examples.expressions
	$(PYTHON) -m user_guide.src.examples.aggregate
	$(PYTHON) -m user_guide.src.examples.column_row_selection
	$(PYTHON) -m user_guide.src.examples.conditionally_apply
	$(PYTHON) -m user_guide.src.examples.df_manipulations
	$(PYTHON) -m user_guide.src.examples.filter
	$(PYTHON) -m user_guide.src.examples.groupby
	$(PYTHON) -m user_guide.src.examples.groupby_dsl
	$(PYTHON) -m user_guide.src.examples.head
	$(PYTHON) -m user_guide.src.examples.join
	$(PYTHON) -m user_guide.src.examples.melt
	$(PYTHON) -m user_guide.src.examples.pivot
	$(PYTHON) -m user_guide.src.examples.predicate_pushdown
	$(PYTHON) -m user_guide.src.examples.projection_pushdown
	$(PYTHON) -m user_guide.src.examples.sorting
	$(PYTHON) -m user_guide.src.examples.strings
	$(PYTHON) -m user_guide.src.examples.strings_performance
	$(PYTHON) -m user_guide.src.examples.timestamps
	$(PYTHON) -m user_guide.src.examples.udfs
	$(PYTHON) -m user_guide.src.examples.window_functions


serve_user_guide: run
	cd ./user_guide; mdbook serve --hostname 0.0.0.0 --port 8000

serve_ref_guide_python: docs
	cd ./reference_guide_python; mdbook serve --hostname 0.0.0.0 --port 8000

serve: serve_user_guide

clean:
	-@rm -fr .venv
	-@rm -fr data
	-@rm -fr user_guide/src/outputs
	-@rm -fr `find . -name __pycache__`
	-@cd user_guide; mdbook clean &>/dev/null
	-@cd reference_guide_python; mdbook clean &>/dev/null
	-@rm -fr reference_guide_python/src

fmt: format

format: .venv
	@.venv/bin/black .
	$(PYTHON) -m mdformat `find user_guide/src -name "*.md" | grep -v SUMMARY.md`
