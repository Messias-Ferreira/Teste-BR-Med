db:
	docker compose up -d postgres_local --build 

web:
	docker compose up -d web --build