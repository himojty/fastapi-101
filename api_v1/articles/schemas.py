from pydantic import BaseModel, Field, ConfigDict


class ArticleSchema(BaseModel):
    title: str = Field(min_length=3, max_length=40)
    body: str = Field(min_length=10)
    user_id: int


class Article(ArticleSchema):
    # model_config = ConfigDict(from_attributes=True)

    id: int


class ArticleCreate(ArticleSchema):
    pass


class ArticleUpdate(ArticleCreate):
    pass


class ArticleUpdatePartial(ArticleCreate):
    title: str | None = None
    body: str | None = None
