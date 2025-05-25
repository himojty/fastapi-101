from contextlib import asynccontextmanager

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from myapp.crud import create_task, get_task
from myapp.database import Base, get_db, engine
from myapp.schemas import TaskRead, CreateTask

@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield

    await engine.dispose()

app = FastAPI(lifespan=lifespan)

@app.post("/tasks/", response_model=TaskRead)
async def create_new_task(
        task_data: CreateTask,
        db: AsyncSession = Depends(get_db)
):
    return await create_task(db, task_data)

@app.get("/tasks/{task_id}", response_model=TaskRead)
async def read_task(
        task_id: int,
        db: AsyncSession = Depends(get_db)
):
    task = await get_task(db, task_id)
    if not task:
        raise HTTPException(status_code=404)
    return task