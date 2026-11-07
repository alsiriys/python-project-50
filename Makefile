install:
	uv sync

gendiff-h:
	uv run gendiff -h

lint:
	uv run ruff check gendiff

build:
	uv build

.PHONY: install gendiff-h lint build