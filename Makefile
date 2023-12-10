format:
	ruff format .

unit-test:
	pytest tests/ -m 'not integration_test'

integration-test:
	pytest tests/ -m 'integration_test'