# FastAPI Base App
[![pytest](https://github.com/pieteradejong/fastapi-base/actions/workflows/pytest.yml/badge.svg?branch=main)](https://github.com/pieteradejong/fastapi-base/actions/workflows/pytest.yml)

**Purpose**: for future use - get started immediately with any new app.

**Audience**: Myself primarily, others welcome.

**Summary**: Use of FastAPI to create a highly performant Python REST API.

## Usage local

```
pip install -r requirements.txt
```
```
uvicorn app.main:app --reload
```
```
pytest app/test.py
```
```
docker-compose up -d --build
```
```
docker-compose exec app pytest test/test.py
```

## API Documentation (Swagger UI)

```
http://127.0.0.1:8000/docs
```

### Run server

```
docker-compose exec db psql --username=fastapi --dbname=fastapi_dev
```

## TODOs
* Fix tests module import
* Ensure using Python 3.11 (latest) throughout
* add basic Pydantic data models for User, Post, Comment
* merge pytest.yml into ci.yml
* add mongo and postgres db's as dependencies for injection
* add env var config for db config etc.

