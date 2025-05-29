from pydantic import BaseModel, Field, ConfigDict


class ArticleSchema(BaseModel):
    title: str = Field(min_length=3, max_length=40)
    content: str = Field(min_length=10)


class Article(ArticleSchema):
    # model_config = ConfigDict(from_attributes=True)

    id: int


class ArticleCreate(ArticleSchema):
    pass


class ArticleUpdate(ArticleCreate):
    pass


class ArticleUpdatePartial(ArticleCreate):
    title: str | None = None
    content: str | None = None
