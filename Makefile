.PHONY: test
test:
	poetry run coverage run -m pytest tests
	poetry run coverage report
	poetry run mypy fluffy_code

.PHONY: test.html
test.html:
	poetry run python -m testing.generate_test_html
