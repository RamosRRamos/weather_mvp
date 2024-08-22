SHELL := /bin/bash # Use bash syntax
ARG := $(word 2, $(MAKECMDGOALS) )
APP_NAME :=
COMMIT_MSG :=

# Macro for adding changes to Git
define GIT_ADD
	@git add $(1)
endef

# Macro to commit changes in Git
define GIT_COMMIT
	@git commit -m "$(1)"
endef

# Macro to push changes to Git
define GIT_PUSH
	@git push
endef

# Task to add, commit and push changes to the backend folder
commit_backend:
	$(call GIT_ADD,backend/)
	$(call GIT_COMMIT,Backend: $(COMMIT_MSG))
	$(call GIT_PUSH)
	@echo "Changes to the backend folder added, committed and sent successfully!"

# Task to add, commit and push changes to the frontend folder
commit_frontend:
	$(call GIT_ADD,frontend/)
	$(call GIT_COMMIT,Frontend: $(COMMIT_MSG))
	$(call GIT_PUSH)
	@echo "Changes to the frontend folder added, committed and sent successfully!"

# Task to add, commit and push all changes
commit_all:
	$(call GIT_ADD,.)
	$(call GIT_COMMIT,All: $(COMMIT_MSG))
	$(call GIT_PUSH)
	@echo "All changes added, committed and sent successfully!"

# Task to create a new branch
new_branch:
	@if [ -z "$(BRANCH_NAME)" ]; then \
		echo "BRANCH_NAME is not defined. Use 'make new_branch BRANCH_NAME=branch_name'"; \
		exit 1; \
	fi; \
	git checkout -b $(BRANCH_NAME) \
	@echo "Nova branch $(BRANCH_NAME) criada com sucesso!"

# Macro for changing branches
# Variable for branch name
BN :=
switch_branch:
	@if [ -z "$(BN)" ]; then \
		echo "BN is not defined. Use 'make switch_branch BN=branch_name'"; \
		exit 1; \
	fi; \
	if git show-ref --verify --quiet "refs/heads/$(BN)"; then \
		git checkout $(BN); \
	else \
		echo "Branch $(BN) not found locally. Creating a new branch..."; \
		git checkout -b $(BN); \
	fi; \
	echo "Switched to branch $(BN) successfully!"

list_remote_branches:
	@git ls-remote --heads origin
	@echo "Remote branches listed successfully!"

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
	echo "Routes.py, serializers.py and tasks.py files successfully created in $(APP_NAME)!"


clean:
	@find . -name "*.pyc" -exec rm -rf {} \;
	@find . -name "__pycache__" -delete

backend_format:
	black backend

# Commands for Docker version
docker_setup:
	docker compose build --no-cache

docker_up:
	docker compose up -d

docker_update_dependencies:
	docker compose down
	docker compose up -d --build

docker_down:
	docker compose down

docker_logs:
	docker compose logs -f $(ARG)

docker_backend_shell:
	docker compose run --rm backend bash

