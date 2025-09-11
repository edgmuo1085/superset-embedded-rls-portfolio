PROJECT_NAME=superset

.PHONY: up build down restart log logs init bash examples delete show

# Levanta el stack
up:
	docker compose up -d

# Levanta el stack build
build:
	#docker compose up -d --build
	docker compose -f docker-compose.yml -f docker-compose.override.yml up -d --build

# Apaga y elimina contenedores + volúmenes
down:
	docker compose down -v

# Reinicia el stack
restart: down up

# Muestra logs en tiempo real
log:
	docker logs -f superset_app

# Muestra logs en tiempo real
logs:
	docker compose logs -f

# Inicializa Superset (solo la primera vez o si reseteas la DB)
init:
	docker exec -it superset_app superset fab create-admin \
		--username admin \
		--firstname Superset \
		--lastname Admin \
		--email admin@local.com \
		--password admin || true
	docker exec -it superset_app superset db upgrade
	docker exec -it superset_app superset init

# Entra al contenedor de superset
bash:
	docker exec -it superset_app bash

# Cargar ejemplos de dashboards y datasets
examples:
	docker exec -it superset_app superset load_examples

# Eliminar volumenes no usuados
delete:
	docker volume prune -f

# Eliminar volumenes no usuados
show:
	docker ps -a --filter volume=superset_superset_home
