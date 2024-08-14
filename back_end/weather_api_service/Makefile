SHELL := /bin/bash # Use bash syntax
ARG := $(word 2, $(MAKECMDGOALS) )
APP_NAME :=
COMMIT_MSG :=

# Macro para adicionar as alterações no Git
define GIT_ADD
	@git add $(1)
endef

# Macro para commitar as alterações no Git
define GIT_COMMIT
	@git commit -m "$(1)"
endef

# Macro para fazer push das alterações no Git
define GIT_PUSH
	@git push
endef

# Tarefa para adicionar, commitar e fazer push das alterações na pasta backend
commit_backend:
	$(call GIT_ADD,backend/)
	$(call GIT_COMMIT,Backend: $(COMMIT_MSG))
	$(call GIT_PUSH)
	@echo "Alterações na pasta backend adicionadas, commitadas e enviadas com sucesso!"

# Tarefa para adicionar, commitar e fazer push das alterações na pasta frontend
commit_frontend:
	$(call GIT_ADD,frontend/)
	$(call GIT_COMMIT,Frontend: $(COMMIT_MSG))
	$(call GIT_PUSH)
	@echo "Alterações na pasta frontend adicionadas, commitadas e enviadas com sucesso!"

# Tarefa para adicionar, commitar e fazer push de todas as alterações
commit_all:
	$(call GIT_ADD,.)
	$(call GIT_COMMIT,All: $(COMMIT_MSG))
	$(call GIT_PUSH)
	@echo "Todas as alterações adicionadas, commitadas e enviadas com sucesso!"

# Tarefa para criar uma nova branch
new_branch:
	@if [ -z "$(BRANCH_NAME)" ]; then \
		echo "BRANCH_NAME não está definido. Use 'make new_branch BRANCH_NAME=nome_da_branch'"; \
		exit 1; \
	fi; \
	git checkout -b $(BRANCH_NAME) \
	@echo "Nova branch $(BRANCH_NAME) criada com sucesso!"

# Macro para trocar de branch
# Variável para o nome da branch
BN :=
switch_branch:
	@if [ -z "$(BN)" ]; then \
		echo "BN não está definido. Use 'make switch_branch BN=nome_da_branch'"; \
		exit 1; \
	fi; \
	if git show-ref --verify --quiet "refs/heads/$(BN)"; then \
		git checkout $(BN); \
	else \
		echo "Branch $(BN) não encontrada localmente. Criando uma nova branch..."; \
		git checkout -b $(BN); \
	fi; \
	echo "Trocado para a branch $(BN) com sucesso!"

list_remote_branches:
	@git ls-remote --heads origin
	@echo "Branches remotas listadas com sucesso!"

createapp:
	@if [ -z "$(APP_NAME)" ]; then \
		echo "APP_NAME não está definido. Use 'make createapp APP_NAME=nome_do_app'"; \
		exit 1; \
	fi; \
	poetry run python backend/manage.py startapp $(APP_NAME); \
	echo "App $(APP_NAME) criado com sucesso!"; \
	touch backend/$(APP_NAME)/routes.py; \
	touch backend/$(APP_NAME)/serializers.py; \
	touch backend/$(APP_NAME)/tasks.py; \
	echo "Arquivos routes.py, serializers.py e tasks.py criados com sucesso em $(APP_NAME)!"


clean:
	@find . -name "*.pyc" -exec rm -rf {} \;
	@find . -name "__pycache__" -delete

test_all_modules:
	poetry run backend/manage.py test backend/ --parallel --keepdb


test:
	poetry run backend/manage.py test backend/ $(ARG) --parallel --keepdb

test_reset:
	poetry run backend/manage.py test backend/ $(ARG) --parallel

backend_format:
	black backend

# Commands for Docker version
docker_setup:
	docker volume create mini_blog_dbdata
	docker compose build --no-cache backend
	docker compose run --rm backend python manage.py spectacular --color --file schema.yml
	docker compose run frontend npm install
	docker compose run --rm frontend npm run openapi-ts

docker_test:
	docker compose run backend python manage.py test $(ARG) --parallel --keepdb

docker_test_reset:
	docker compose run backend python manage.py test $(ARG) --parallel

docker_up:
	docker compose up -d

docker_update_dependencies:
	docker compose down
	docker compose up -d --build

docker_update_dependencies_witch_cache:
	docker compose down
	docker-compose build --no-cache
	docker-compose up -d

docker_down:
	docker compose down

docker_logs:
	docker compose logs -f $(ARG)

docker_makemigrations:
	docker compose run --rm backend python manage.py makemigrations

docker_migrate:
	docker compose run --rm backend python manage.py migrate

docker_backend_shell:
	docker compose run --rm backend bash

docker_backend_update_schema:
	docker compose run --rm backend python manage.py spectacular --color --file schema.yml

docker_frontend_update_api:
	docker compose run --rm frontend npm run openapi-ts
