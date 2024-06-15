run:
	@uvicorn store.main:app --reload

precommit-install:
	@poetry run pre-commit install

test:
	@PYTHONPATH=. pytest

test-matching:
	@poetry run pytest -s -rx -k $(K) --pdb store ./tests/
