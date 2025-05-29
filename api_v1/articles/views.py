from typing import Annotated

from fastapi import APIRouter, status, Path, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from . import crud
from core.models import db_helper
from .dependencies import article_by_id
from .schemas import ArticleCreate, Article, ArticleUpdate, ArticleUpdatePartial

router = APIRouter(prefix="/articles", tags=["Articles"])


@router.post(
    "/",
    response_model=ArticleCreate,
    status_code=status.HTTP_201_CREATED,
)
async def create_article(
    article: ArticleCreate,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.create_article(session=session, article_in=article)


@router.get("/")
async def get_articles(
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.get_articles(session=session)


@router.get("/{article_id}/", response_model=Article)
async def get_article(
    article: Article = Depends(article_by_id),
):
    return article


@router.put("/{article_id}/", response_model=Article)
async def update_article(
    article_update: ArticleUpdate,
    article: Article = Depends(article_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.update_article(
        session=session,
        article=article,
        article_update=article_update,
    )


@router.patch("/{article_id}/")
async def update_article_partial(
    article_update: ArticleUpdatePartial,
    article: Article = Depends(article_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.update_article(
        session=session,
        article=article,
        article_update=article_update,
        partial=True,
    )


@router.delete("/{article_id}/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_article(
    article: Article = Depends(article_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> None:
    await crud.delete_article(session=session, article=article)
