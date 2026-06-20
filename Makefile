.PHONY: all clean test lint

all: test lint

clean:
	rm -rf .direnv
	rm -rf .mypy_cache
	rm -rf .pytest_cache
	rm -rf .ruff_cache
	rm -rf __pycache__
	rm -rf tests/__pycache__

test:
	python -m pytest

lint:
	black --check csshi tests/
	isort --check --profile=black csshi
	cd tests && isort --check --profile=black *.py
	ruff check csshi tests/
	mypy csshi tests/
