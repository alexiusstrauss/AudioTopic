SHELL := /bin/bash
FILES=$(shell docker ps -a -q --filter "name=audiotopic-api*")

# Verifica versao do docker compose.
COMPOSE_COMMAND=$(shell command -v docker-compose >/dev/null 2>&1 && echo "docker-compose" || echo "docker compose")

clean:
	@find . -name '*.pyc' -exec rm -rf {} \;
	@find . -name '__pycache__' -exec rm -rf {} \;
	@find . -name 'Thumbs.db' -exec rm -rf {} \;
	@find . -name '*~' -exec rm -rf {} \;
	rm -rf .cache
	rm -rf build
	rm -rf dist
	rm -rf *.egg-info
	rm -rf htmlcov
	rm -rf .coverage
	rm -rf .pytest_cache
	rm -rf dev.sqlite3
	rm -rf src/.pytest_cache
	rm -rf src/dev.sqlite3	

create-requirements:
	pipenv requirements > contrib/requirements.txt

build:
	docker build -t audiotopic-api:latest .

up: build
	docker compose up $(dettach) -d audiotopic-api

down:
	docker compose down

run-dev:
	uvicorn src.api:app --reload

bash:
	docker exec -ti audiotopic-api bash

logs-app:
	docker logs -f audiotopic-api

test:
	pytest -vv

isort:
	@isort -m 3 --trailing-comma --use-parentheses --honor-noqa  src/. --verbose --diff
	
style:  ## Run isort and black auto formatting code style in the project
	@isort -m 3 --trailing-comma --use-parentheses --honor-noqa  src/.
	@black -S -t py37 -l 120 src/. --exclude '/(\.git|\.venv|env|venv|build|dist)/'

.PHONY: all clean install test 