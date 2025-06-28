from contextlib import asynccontextmanager

from fastapi import FastAPI

import uvicorn
from starlette.middleware.cors import CORSMiddleware

from core.config import settings
from core.models import Base, db_helper

from api_v1 import router as api_v1_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(router=api_v1_router, prefix="/api-v1")

allow_origins = [
    "http://localhost:63342",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=allow_origins,  # ['*'] Разрешить все домены
    allow_methods=["GET"],  # ['*'] Разрешить все методы (GET, POST и т.д.)
    # allow_headers=["*"],  # Разрешить все заголовки
)


@app.get("/")
async def home():
    return {"message": "Hello world!"}


if __name__ == "__main__":
    uvicorn.run(app="main:app", reload=True)
