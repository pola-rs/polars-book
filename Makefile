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

# adding the download of astdocs here (instead of in the .venv recipe) as it might still change fairly often
docs: .venv
	@wget -q https://raw.githubusercontent.com/carnarez/astdocs/master/astdocs.py -O .venv/lib/python3.8/site-packages/astdocs.py
	-@rm -fr reference_guide_python/src
	ASTDOCS_SPLIT_BY=mc ASTDOCS_WITH_LINENOS=on $(PYTHON) generate_ref_guide_python.py

run: data
	$(PYTHON) -m user_guide.src.examples.aggregate
	$(PYTHON) -m user_guide.src.examples.how_can_i.conditionally_apply
	$(PYTHON) -m user_guide.src.examples.expressions
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
	$(PYTHON) -m user_guide.src.examples.how_can_i.filter
	$(PYTHON) -m user_guide.src.examples.how_can_i.sorting
	$(PYTHON) -m user_guide.src.examples.how_can_i.joins
	$(PYTHON) -m user_guide.src.examples.how_can_i.melt
	$(PYTHON) -m user_guide.src.examples.how_can_i.pivot

serve_user_guide: run
	cd /usr/src/user_guide; mdbook serve --hostname 0.0.0.0 --port 8000

serve_ref_guide_python: docs
	cd /usr/src/reference_guide_python; mdbook serve --hostname 0.0.0.0 --port 8000

serve: serve_user_guide

clean:
	-@rm -fr .venv
	-@rm -fr data
	-@rm -fr user_guide/src/outputs
	-@rm -fr `find . -name __pycache__`
	-@cd user_guide; mdbook clean
	-@cd reference_guide_python; mdbook clean
	-@rm -fr reference_guide_python/src

format:
	black .
	mdformat `find user_guide/src -name "*.md" | grep -v SUMMARY.md`
