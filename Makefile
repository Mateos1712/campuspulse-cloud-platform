.PHONY: install test lint security local-up local-down smoke fmt

install:
	python3 -m pip install -e '.[dev]'

test:
	pytest -q --cov=app --cov-report=term-missing

lint:
	ruff check .

security:
	bandit -q -r app
	pip-audit

local-up:
	docker compose up --build -d

local-down:
	docker compose down -v

smoke:
	./scripts/smoke_test.sh http://localhost:8000

fmt:
	ruff format .
	terraform fmt -recursive infra/terraform

