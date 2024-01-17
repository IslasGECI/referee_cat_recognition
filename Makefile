all: check coverage mutants

.PHONY: \
		all \
		check \
		clean \
		coverage \
		evaluate_classifier \
		format \
		init \
		install \
		linter \
		mutants \
		setup \
		tests

module = geci_referee
codecov_token = 6c56bccb-1758-4ed9-8161-97c845591c26

define lint
	pylint \
        --disable=bad-continuation \
        --disable=missing-class-docstring \
        --disable=missing-function-docstring \
        --disable=missing-module-docstring \
        ${1}
endef

check:
	black --check --line-length 100 ${module}
	black --check --line-length 100 tests
	flake8 --max-line-length 100 ${module}
	flake8 --max-line-length 100 tests
	mypy ${module}
	mypy tests

clean:
	rm --force --recursive .*_cache
	rm --force --recursive ${module}.egg-info
	rm --force --recursive ${module}/__pycache__
	rm --force --recursive tests/__pycache__
	rm --force .mutmut-cache
	rm --force coverage.xml

coverage: setup
	pytest --cov=${module} --cov-report=xml --verbose && \
	coverage report --show-missing

evaluate_classifier:
	python src/evaluate_classifier.py
	@echo "Predicted positive:"
	ls /workdir/cat_detected
	@echo "All photos:"
	ls /workdir/camera_trap_photos
	@echo "True positive:"
	grep ",1" /workdir/data/all_photos.csv
	@echo "True negative:"
	grep ",0" /workdir/data/all_photos.csv

format:
	black --line-length 100 ${module}
	black --line-length 100 tests

init: setup tests
	git config --global --add safe.directory /workdir
	git config --global user.name "Ciencia de Datos • GECI"
	git config --global user.email "ciencia.datos@islas.org.mx"

install:
	pip install --editable .

linter:
	$(call lint, ${module})
	$(call lint, tests)

mutants: setup
	mutmut run --paths-to-mutate ${module}

setup: clean install

tests:
	pytest --verbose

red: format
	pytest --verbose \
	&& git restore tests/*.py \
	|| (git add tests/*.py && git commit -m "🛑🧪 Fail tests")
	chmod g+w -R .

green: format
	pytest --verbose \
	&& (git add ${module}/*.py tests/*.py && git commit -m "✅ Pass tests") \
	|| git restore ${module}/*.py
	chmod g+w -R .

refactor: format
	pytest --verbose \
	&& (git add ${module}/*.py tests/*.py && git commit -m "♻️  Refactor") \
	|| git restore ${module}/*.py tests/*.py
	chmod g+w -R .
