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
	-@mkdir -p user_guide/src/outputs
	$(PYTHON) -m user_guide.src.examples.lazy_chapter.data_head
	$(PYTHON) -m user_guide.src.examples.lazy_chapter.predicate_pushdown_0
	$(PYTHON) -m user_guide.src.examples.lazy_chapter.predicate_pushdown_1
	$(PYTHON) -m user_guide.src.examples.lazy_chapter.projection_pushdown_0
	$(PYTHON) -m user_guide.src.examples.how_can_i.groupby
	$(PYTHON) -m user_guide.src.examples.how_can_i.aggregate
	$(PYTHON) -m user_guide.src.examples.how_can_i.parse_dates
	$(PYTHON) -m user_guide.src.examples.how_can_i.conditionally_apply
	$(PYTHON) -m user_guide.src.examples.how_can_i.use_custom_functions
	$(PYTHON) -m user_guide.src.examples.how_can_i.use_custom_functions_1
	$(PYTHON) -m user_guide.src.examples.how_can_i.use_custom_functions_2
	$(PYTHON) -m user_guide.src.examples.how_can_i.use_custom_functions_3
	$(PYTHON) -m user_guide.src.examples.how_can_i.process_strings
	$(PYTHON) -m user_guide.src.examples.how_can_i.apply_window_functions
	$(PYTHON) -m user_guide.src.examples.how_can_i.det_group_statistics
	$(PYTHON) -m user_guide.src.examples.groupby.dsl

clean:
	-@rm -fr .venv
	-@rm -fr data
	-@rm -fr `find . -name __pycache__`
	-@cd user_guide; mdbook clean
