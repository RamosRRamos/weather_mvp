SHELL := /bin/bash # Use bash syntax
ARG := $(word 2, $(MAKECMDGOALS) )
APP_NAME :=

# Commands for Docker version
docker_setup:
	docker build --no-cache backend
	docker run -d -p 8000:8000 --name main_service

docker_test:
	docker run main_service python manage.py test $(ARG) --parallel --keepdb

docker_test_reset:
	docker run main_service python manage.py test $(ARG) --parallel

docker_up:
	docker run -d -p 8000:8000 --name main_service

docker_update_dependencies:
	docker stop main_service
	docker run -d --build main_service

docker_down:
	docker stop main_service

docker_logs:
	docker logs -f $(ARG)

docker_makemigrations:
	docker exec -it main_service python manage.py makemigrations

docker_migrate:
	docker exec -it main_service python manage.py migrate

docker_backend_shell:
	docker exec -it main_service python manage.py shell

