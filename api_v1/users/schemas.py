from pydantic import BaseModel


class UserSchema(BaseModel):
    username: str


class User(UserSchema):
    id: int


class UserCreate(User):
    pass
