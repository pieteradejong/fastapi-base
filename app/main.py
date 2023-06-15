import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
.
app = FastAPI()

@app.get("/")
def home():
    return {"Hello": "World!"}

if __name__ == "__main__":
    uvicorn.run("app:app")
