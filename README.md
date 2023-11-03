# FastAPI Base App
[![pytest](https://github.com/pieteradejong/fastapi-base/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/pieteradejong/fastapi-base/actions/workflows/ci.yml)

**Purpose**: Use as backend base for future apps using a Python FastAPI REST API.

## Quickly run with Docker

```sh
git clone https://github.com/your-username/your-fastapi-app.git
cd your-fastapi-app
```

```sh
docker build -t fastapi-based .
```

```sh
docker run -d --name fastapi-based-container -p 80:80 fastapi-based
```

**Now you can view the app at http://127.0.0.1:8000/, and Swagger UI docs at `/docs`.


```sh
docker stop fastapi-based-container
```

```sh
docker rm fastapi-based-container
```


## Run/dev/test local, no Docker

From `fastapi-base` folder:
```sh
uvicorn app.main:app --reload
```

From `fastapi-base` folder:
```sh
pytest
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
* potentially add Pydantic's config capabilities.

