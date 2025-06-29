from pydantic import BaseModel


class ItemSchema(BaseModel):
    title: str
    description: str
    user_id: int


class Item(ItemSchema):
    id: int


class ItemCreate(ItemSchema):
    pass
