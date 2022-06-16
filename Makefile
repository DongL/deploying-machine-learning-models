.PHONY: lint autolint install

lint:
	poetry run flake8 scripts test

autolint:
	poetry run autopep8 -r -i .

install:
	pip install poetry
	poetry install