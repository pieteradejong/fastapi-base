# FastAPI Base App
[![pytest](https://github.com/pieteradejong/fastapi-base/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/pieteradejong/fastapi-base/actions/workflows/ci.yml)

**Purpose**: Use as backend base for future apps using a Python FastAPI REST API.

## Quickly run with Docker

Clone repo:
```sh
git clone git@github.com:pieteradejong/fastapi-base.git
```

Build: within  `fastapi-base` directory:
```sh
docker build -t fastapi-base .
```

Run:
```sh
docker run -p 8000:80  fastapi-base
```

Explore contents of running container (fill in container id, and whichever command after `-c`):
```sh
docker exec -it <CONTAINER_ID> /bin/sh -c "ls /app"
```

Visit endpoints at [http://127.0.0.1:8000/](http://127.0.0.1:8000) and [/health](http://127.0.0.1:8000/health), and Swagger UI doc at [/docs](http://127.0.0.1:8000/docs).


```sh
docker stop <container name>
```

```sh
docker rm <container_name>
```


## Run/dev/test local, no Docker

Run server, from `fastapi-base` folder:
```sh
uvicorn app.main:app --reload
```

Test, from `fastapi-base` folder:
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

