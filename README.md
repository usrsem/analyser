# Analyser project

## What it does
This microservice was created for the analytics of citizens. Implemented
a number of endpoints for adding, viewing and changing citizens in the
database. Endpoints will also be implemented to collect analytics based on
uploaded data.


## What used
* FastAPI
* Pydantic
* PostgreSQL
* SqlAlchemy
* Alembic
* Poetry
* Uvicorn


## How to run
Add path vars:
1. `ANALYSER_PG_USER`
1. `ANALYSER_PG_PASSWORD`
1. `ANALYSER_PG_HOST`
1. `ANALYSER_PG_DB_NAME`

Then run commands:
```
poetry install --no-dev
poetry run alembic upgrade head
poetry run api
```

## Docs
Swagger docs available on http://localhost:8000/docs by default

