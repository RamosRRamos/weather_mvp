SHELL := /bin/bash # Use bash syntax
ARG := $(word 2, $(MAKECMDGOALS) )
APP_NAME :=


test_all_modules:
	poetry run manage.py test --parallel --keepdb


test:
	poetry run manage.py test $(ARG) --parallel --keepdb

test_reset:
	poetry run backend/manage.py test $(ARG) --parallel

backend_format:
	black backend

# Commands for Docker version
docker_setup:
	docker build --no-cache backend
	docker run -d -p 8000:8000 --name openai_service

docker_test:
	docker run openai_service python manage.py test $(ARG) --parallel --keepdb

docker_test_reset:
	docker run openai_service python manage.py test $(ARG) --parallel

docker_up:
	docker run -d -p 8000:8000 --name openai_service

docker_update_dependencies:
	docker stop openai_service
	docker run -d --build openai_service

docker_down:
	docker stop openai_service

docker_logs:
	docker logs -f $(ARG)

docker_makemigrations:
	docker exec -it openai_service python manage.py makemigrations

docker_migrate:
	docker exec -it openai_service python manage.py migrate

docker_backend_shell:
	docker exec -it openai_service python manage.py shell

