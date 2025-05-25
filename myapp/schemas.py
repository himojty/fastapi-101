from pydantic import BaseModel


class CreateTask(BaseModel):
    name: str
    description: str

class TaskRead(BaseModel):
    id: int
    name: str
    description: str
