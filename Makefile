.DEFAULT_GOAL := help

HOST ?= 127.0.0.1
PORT ?= 8000

run: ## run local uvicorn server
	uvicorn main:app --host $(HOST) --port $(PORT) --reload --env-file .local.env


install: ## install library from poetry
	@echo "Installing dependency $(LIBRARY)"
	poetry add $(LIBRARY)


uninstall: ## delete library from poetry
	@echo "Uninstalling dependency $(LIBRARY)"
	poetry remove $(LIBRARY)

update: ## updates poetry
	@echo "updating poetry"
	poetry update

delete_poetry_0000: ## deleting poetry
	@echo "deleting poetry"
	uninstall poetry


help: ## Show this help message
	@echo "Usage: make [conmand]" 
	@echo ""
	@echo "Commands:"
	@grep -E '^[a-zA-Z0-9_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf" %-20s %s\n", $$1, $$2}'

