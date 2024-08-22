SHELL := /bin/bash # Use bash syntax
ARG := $(word 2, $(MAKECMDGOALS) )
APP_NAME :=

createapp:
	@if [ -z "$(APP_NAME)" ]; then \
		echo "APP_NAME is not defined. Use 'make createapp APP_NAME=app_name'"; \
		exit 1; \
	fi; \
	poetry run python backend/manage.py startapp $(APP_NAME); \
	echo "App $(APP_NAME) created successfully!"; \
	touch backend/$(APP_NAME)/routes.py; \
	touch backend/$(APP_NAME)/serializers.py; \
	touch backend/$(APP_NAME)/tasks.py; \
	echo "routes.py, serializers.py and tasks.py files successfully created in $(APP_NAME)!"


clean:
	@find . -name "*.pyc" -exec rm -rf {} \;
	@find . -name "__pycache__" -delete

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
	docker run -d -p 8000:8000 --name weather_api_service

docker_test:
	docker run weather_api_service python manage.py test $(ARG) --parallel --keepdb

docker_test_reset:
	docker run weather_api_service python manage.py test $(ARG) --parallel

docker_up:
	docker run -d -p 8000:8000 --name weather_api_service

docker_update_dependencies:
	docker stop weather_api_service
	docker run -d --build weather_api_service

docker_down:
	docker stop weather_api_service

docker_logs:
	docker logs -f $(ARG)

docker_makemigrations:
	docker exec -it weather_api_service python manage.py makemigrations

docker_migrate:
	docker exec -it weather_api_service python manage.py migrate

docker_backend_shell:
	docker exec -it weather_api_service python manage.py shell

