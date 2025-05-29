from contextlib import asynccontextmanager

from fastapi import FastAPI

import uvicorn

from core.config import settings
from core.models import Base, db_helper

from api_v1 import router as api_v1_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with db_helper.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    yield


app = FastAPI(lifespan=lifespan)
app.include_router(router=api_v1_router, prefix="/api-v1")


@app.get("/")
async def home():
    return {"message": "Hello world!"}


if __name__ == "__main__":
    uvicorn.run(app="main:app", reload=True)
