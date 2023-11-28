SHELL := /bin/bash
FILES=$(shell docker ps -a -q --filter "name=audiotopic*")

# Verifica versao do docker compose.
COMPOSE_COMMAND=$(shell command -v docker-compose >/dev/null 2>&1 && echo "docker-compose" || echo "docker compose")

build:
	docker build -t audiotopic-api:latest ./backend
	docker build -t audiotopic-app:latest ./frontend

up: build
	docker compose up $(dettach) audiotopic-app

down:
	docker compose down -v

bash-api:
	docker exec -ti audiotopic-api bash

bash-app:
	docker exec -ti audiotopic-app bash

test-api:
	docker exec -ti audiotopic-api pipenv run pytest

logs-api:
	docker logs -f audiotopic-api

logs-app:
	docker logs -f audiotopic-app

.PHONY: all clean install test 