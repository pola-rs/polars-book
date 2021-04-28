SHELL=/bin/bash
PYTHON=.venv/bin/python

.venv:
	@python3  -m venv .venv
	@.venv/bin/pip install -U pip;
	@.venv/bin/pip install -r requirements.txt;

.PHONY: data
data: .venv
	@bash download.sh
	@$(PYTHON) create_data.py

.PHONY: clean
clean:
	@rm -r .venv
	@rm -r data


run: .venv
	@mkdir -p book/src/outputs
	$(PYTHON) -m book.src.examples.lazy_chapter.data_head
	$(PYTHON) -m book.src.examples.lazy_chapter.predicate_pushdown_0
	$(PYTHON) -m book.src.examples.lazy_chapter.predicate_pushdown_1
	$(PYTHON) -m book.src.examples.lazy_chapter.projection_pushdown_0
	$(PYTHON) -m book.src.examples.how_can_i.groupby
	$(PYTHON) -m book.src.examples.how_can_i.aggregate
	$(PYTHON) -m book.src.examples.how_can_i.parse_dates
	$(PYTHON) -m book.src.examples.how_can_i.conditionally_apply
	$(PYTHON) -m book.src.examples.how_can_i.use_custom_functions
	$(PYTHON) -m book.src.examples.how_can_i.use_custom_functions_1
	$(PYTHON) -m book.src.examples.how_can_i.use_custom_functions_2
	$(PYTHON) -m book.src.examples.how_can_i.use_custom_functions_3
	$(PYTHON) -m book.src.examples.how_can_i.process_strings
	$(PYTHON) -m book.src.examples.how_can_i.apply_window_functions
	$(PYTHON) -m book.src.examples.how_can_i.det_group_statistics
	$(PYTHON) -m book.src.examples.groupby.dsl
