SHELL=/bin/bash
PYTHON=.venv/bin/python

.venv:
	@python3  -m venv .venv
	@.venv/bin/pip install -r requirements.txt;

.PHONY: data
data: .venv
	-@mkdir "data"
	@$(PYTHON) create_data.py
	$(PYTHON) -m micro_bench.csv_read
	$(PYTHON) -m micro_bench.groupby_pandas
	$(PYTHON) -m micro_bench.groupby_polars
	$(PYTHON) -m micro_bench.join

.PHONY: clean
	@rm -r .venv
	@rm -r data


run:
	@mkdir -p book/src/outputs
	$(PYTHON) -m micro_bench.plot_results
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
	$(PYTHON) -m book.src.examples.how_can_i.process_strings
