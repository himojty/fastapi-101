from pydantic import BaseModel


class ItemSchema(BaseModel):
    name: str
    description: str


class Item(ItemSchema):
    id: int


class ItemCreate(ItemSchema):
    pass
