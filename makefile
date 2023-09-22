local:
	docker compose up -d --build 

db:
	docker compose up -d postgres_local --build 

web:
	docker compose up -d web --build

makemigrations:
	docker compose exec web python manage.py makemigrations

popular_base:
	docker compose exec web python manage.py popular_base 30

testes:
	docker compose exec web python manage.py test conversor