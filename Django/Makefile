.PHONY: install
install:
	poetry install

.PHONY: migrate
migrate:
	poetry run python -m core.manage migrate

migrations:
	poetry run python -m core.manage.makemigrations

run-server:
	poetry run python -m core.manage runserver

.PHONY: superuser
superuser:
	poetry run python -m core.manage createsuperuser

update: install migrate ;