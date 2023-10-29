import uvicorn
from fastapi import FastAPI
from app.api import api
from fastapi.staticfiles import StaticFiles
from pathlib import Path
from app.config import logger

app = FastAPI()

app.include_router(api.router)
app.mount(
    "/static",
    StaticFiles(directory=Path(__file__).parent.parent.absolute() / "app/static"),
    name="static",
)


@app.on_event("startup")
async def startup_event():
    logger.info("Starting application...")


@app.on_event("shutdown")
async def shutdown_event():
    logger.info("Shutting down application...")


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
