from sqlalchemy.ext.asyncio import AsyncSession
from .models import Task
from myapp.schemas import CreateTask
from sqlalchemy import select



async def create_task(db: AsyncSession, task_data: CreateTask):
    task = Task(**task_data.model_dump())
    db.add(task)
    await db.commit()
    await db.refresh()
    return task

async def get_task(db: AsyncSession, task_id: int):
    result = await db.execute(select(Task).where(Task.id == task_id))