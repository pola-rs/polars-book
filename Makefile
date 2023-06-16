.PHONY: requirements serve lint

requirements:
	python3 -m venv .venv
	. .venv/bin/activate
	pip install -r requirements.txt
	npm install --save-dev --save-exact rome

serve: requirements
	. .venv/bin/activate && mkdocs serve

lint:
# python
	black --check . 
# js
	npx rome format docs/src/node/