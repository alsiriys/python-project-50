install:
	uv sync

gendiff-h:
	uv run gendiff -h

lint:
	uv run ruff check gendiff

test:
	uv run pytest

test-coverage:
	uv run pytest --cov=gendiff --cov-report=xml
	
build:
	uv build

.PHONY: install gendiff-h lint test test-coverage build