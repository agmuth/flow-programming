install:
	poetry install

format:
	poetry run black flowprog/
	poetry run black tests/

	poetry run isort flowprog/
	poetry run isort tests/

lint:
	poetry run ruff --fix flowprog/
	poetry run ruff --fix tests/

test:
	poetry run pytest --cov=tests tests/