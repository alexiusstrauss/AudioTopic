SHELL := /bin/bash
FILES=$(shell docker ps -a -q --filter "name=audiotopic-app*")

# Verifica versao do docker compose.
COMPOSE_COMMAND=$(shell command -v docker-compose >/dev/null 2>&1 && echo "docker-compose" || echo "docker compose")

build:
	docker build -t audiotopic-app:latest .

up: build
	docker compose up $(dettach) -d audiotopic-app

down:
	docker compose down

bash:
	docker exec -ti audiotopic-app bash

logs-app:
	docker logs -f audiotopic-app


.PHONY: all clean install test 