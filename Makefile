.PHONY: test
test:
	poetry run coverage run -m pytest tests
	poetry run coverage report
	poetry run mypy fluffy_code

